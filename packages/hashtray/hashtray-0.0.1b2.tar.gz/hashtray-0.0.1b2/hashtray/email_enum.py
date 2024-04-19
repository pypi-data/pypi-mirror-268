import hashlib
import itertools
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import tqdm
from rich.console import Console as c
from unidecode import unidecode

from hashtray.gravatar import Gravatar


class EmailEnum:
    def __init__(
        self,
        account_hash,
        strings: list = None,
        domain_list: str = None,
        custom_domains: list = None,
    ):
        self.account_hash = self.hashed = account_hash
        self.separators = ["", ".", "_", "-"]
        self.name_pattern = "[-_ ./]"
        self.emails = []
        self.elements = strings
        self.public_emails = []
        if custom_domains:
            self.domains = custom_domains
        else:
            self.domain_list = domain_list
            self.domains = self.load_domains()
        self.len_domains = len(self.domains)
        self.g = None
        self.bar = None
        self.n = 0
        self.rate = 0
        self.elapsed = 0
        self.c = c(highlight=False)

    def load_domains(self):
        # Load domains from json files
        domain_files = {None: "", "common": "", "long": "_long", "full": "_full"}
        domain_file = domain_files[self.domain_list]
        with open(
            Path(Path(__file__).parent, "data", f"email_services{domain_file}.json"),
            "r",
        ) as f:
            return json.load(f)

    def create_elements(self) -> list:
        # Get Gravatar info with account or with account hash
        if self.check_mailhash(self.account_hash):
            self.g = Gravatar(ghash=self.account_hash)
        else:
            self.g = Gravatar(account=self.account_hash)
        if not self.g.get_json():
            self.bar.close()
            self.c.print(
                f"Account {self.account_hash} not found on Gravatar.com\n", style="red"
            )
            sys.exit(1)
        # Get elements with custom arguments or from the Gravatar profile
        if self.elements:
            elements = self.get_custom_elements()
        else:
            elements = self.get_elements_from_gravatar()
        return elements

    def get_custom_elements(self):
        # Get elements from custom arguments
        self.elements = [
            unidecode(element.lower())
            for element in self.elements
            if element is not None
        ]
        elements = []
        if any(element is not None for element in self.elements):
            elements.extend(
                [element for element in self.elements if element not in elements]
            )
        return elements

    def get_elements_from_gravatar(self):
        # Get elements from the Gravatar profile
        elements = []
        infos = self.g.info()
        self.get_public_emails(infos)
        self.hashed = infos["hash"]
        gob = self.process_gravatar_info(infos)
        for element in gob:
            deco = unidecode(element.lower())
            elements.append(deco) if deco not in elements else None
        return elements

    def get_public_emails(self, infos):
        # Get emails from the Gravatar json emails
        if infos["emails"]:
            self.public_emails.extend(
                infos["emails"][email]
                for email in infos["emails"]
                if self.check_email(infos["emails"][email])
            )
        # Get emails from the Gravatar json aboutMe bio
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        find = re.findall(pattern, infos["aboutMe"]) if infos["aboutMe"] else None
        self.public_emails.extend(find) if find else None

    def process_gravatar_info(self, infos):
        # Process Gravatar infos to get additional chunks
        gob = []
        self.add_preferred_username(infos, gob)
        self.add_profile_url(infos, gob)
        self.add_display_name(infos, gob)
        self.add_given_name(infos, gob)
        self.add_family_name(infos, gob)
        self.add_accounts(infos, gob)
        self.add_elements(gob)
        return gob

    def add_preferred_username(self, infos, gob):
        if infos["preferredUsername"]:
            gob.append(infos["preferredUsername"])

    def add_profile_url(self, infos, gob):
        if infos["profileUrl"]:
            gob.append(self.last_url_chunk(infos["profileUrl"]))

    def add_chunks(self, string, gob):
        if string:
            names = re.split(self.name_pattern, unidecode(string))
            chunks = [name for name in names if name]
            # Add first letter (here in case, but it adds too many combinations)
            # chunks.extend(name[:1] for name in names if len(name) > 1)
            gob.extend(chunks)

    def add_display_name(self, infos, gob):
        self.add_chunks(infos["displayName"], gob)

    def add_given_name(self, infos, gob):
        # Add given name and first letter chunks
        if infos["name"] and infos["name"]["givenName"]:
            self.add_chunks(infos["name"]["givenName"], gob)
            self.add_chunks(
                infos["name"]["givenName"][0],
                gob if len(infos["name"]["givenName"]) > 1 else None,
            )

    def add_family_name(self, infos, gob):
        # Add family name and first letter chunks
        if infos["name"] and infos["name"]["familyName"]:
            self.add_chunks(infos["name"]["familyName"], gob)
            self.add_chunks(
                infos["name"]["familyName"][0],
                gob if len(infos["name"]["familyName"]) > 1 else None,
            )

    def add_accounts(self, infos, gob):
        # Add account chunks for verified accounts
        if infos["accounts"]:
            for account in infos["accounts"]:
                account_url = infos["accounts"][account].rstrip("/")
                self.process_account(account, account_url, gob)

    def process_account(self, account, account_url, gob):
        # Verified accounts username chunks
        if account in ["Mastodon", "Fediverse"]:
            gob.append(self.last_url_chunk(account_url).replace("@", ""))
        elif account in ["LinkedIn", "YouTube"]:
            (
                gob.append(self.last_url_chunk(account_url))
                if f"{account.lower()}.com/in/" in account_url
                else None
            )
        elif account == "Tumblr":
            gob.append(urlparse(account_url).netloc.split(".")[0])
        elif account in ["Facebook", "Instagram"]:
            if "profile.php" not in account_url:
                gob.extend(
                    chunk for chunk in self.last_url_chunk(account_url).split(".")
                )
        elif account == "Stack Overflow":
            gob.extend(chunk for chunk in self.last_url_chunk(account_url).split("-"))
        elif account == "Flickr":
            if "/people/" not in account_url:
                gob.extend(
                    chunk for chunk in self.last_url_chunk(account_url).split("-")
                )
        elif account == "Twitter":
            gob.extend(chunk for chunk in self.last_url_chunk(account_url).split("_"))
        elif account == "Goodreads":
            gob.extend(
                chunk for chunk in self.last_url_chunk(account_url).split("-")[1:]
            )
        elif account not in [
            "TikTok",
            "Foursquare",
            "WordPress",
            "Yahoo",
            "Google+",
            "Vimeo",
        ]:
            chunk = self.last_url_chunk(account_url)
            gob.append(chunk)

    def add_elements(self, gob):
        # Building final list of chunks, deduped , lowercase and unidecoded
        self.elements = []
        self.elements = [
            unidecode(element.lower())
            for element in gob
            if unidecode(element.lower()) not in self.elements
        ]

    def hash_email(self, email):
        # MD5 hashing of a string email
        return hashlib.md5(email.lower().encode()).hexdigest()

    def check_mailhash(self, s: str):
        # Check if a string is a valid MD5 hash
        return re.fullmatch(r"[a-fA-F0-9]{32}", s) is not None

    def check_email(self, email):
        # Check if a string is a valid email
        return (
            True
            if re.match(r"(^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
            else False
        )

    def last_url_chunk(self, s: str):
        # Get the last chunk of an URL
        return s.split("/")[-1]

    def is_combination(self, s, chunks):
        # Logic to check if a string is a combination of other strings
        if s in chunks:
            chunks.remove(s)
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if left in chunks and right in chunks:
                return True
            if left in chunks and self.is_combination(right, chunks):
                return True
            if right in chunks and self.is_combination(left, chunks):
                return True
        return False

    def dedup_chunks(self, chunks):
        # Remove chunks from a list of chunks if it's made with other strings of the list
        return [s for s in chunks if not self.is_combination(s, chunks.copy())]

    def show_chunks(self, elements):
        # Show chunks as a string
        em = ""
        for element in elements:
            em += element + ", "
        return em.rstrip(", ")

    def get_combination_count(self, n):
        # Calculate the total number of combinations for tdqm bar progress
        total = 0
        for r in range(1, n + 1):
            if r == 1:
                # Add single chunks
                total += n
            else:
                # Calc. combinations
                combinations = itertools.combinations(range(n), r)
                # Calc. permutations
                permutations = itertools.permutations(range(r))
                # Total possibilities for n chunks
                combination_count = len(list(combinations)) * len(list(permutations))
                # x number of special chars
                total += combination_count * len(self.separators)
        # Multiply by the number of domains
        return total * len(self.domains)

    def combinator(self):
        # Generate all possible email combinations for unique elements
        # Get chunks and dedup them if made with other chunks
        elements = self.dedup_chunks(self.create_elements())
        n_combs = self.get_combination_count(len(elements))
        self.bar.total = n_combs
        self.bar.write(
            f"Chunks: {self.show_chunks(elements)} / domains : {self.len_domains} / combinations : {n_combs}.\n"
        )
        # Generate all permutations/combinations of elements
        # Per chunk
        for r in range(1, len(elements) + 1):
            # print(self.bar.format_dict)

            # Per chunk permutation
            for permutation in itertools.permutations(elements, r):
                # Per domain
                for domain in self.domains:
                    # No need of separator for single chunks
                    if len(permutation) == 1:
                        email_local_part = permutation[0]
                        yield f"{email_local_part}@{domain}"
                    else:
                        # Per separator
                        for separator in self.separators:
                            email_local_part = separator.join(permutation)
                            yield f"{email_local_part}@{domain}"

    def hashes(self):
        # Calculate emails hash
        for email in self.combinator():
            hashd = self.hash_email(email)
            self.bar.update()
            # Return if found
            if self.hashed == hashd:
                # Get progress bar info
                self.n = self.bar.format_dict["n"]
                self.rate = self.bar.format_dict["rate"]
                self.elapsed = self.bar.format_dict["elapsed"]
                self.bar.close()
                return email
        self.bar.close()

    def find(self):
        # Print process and results
        self.c.print(
            f"Finding email for [bright_white]{self.account_hash}[/bright_white]\n"
        )
        # Init progress bar
        self.bar = tqdm.tqdm(
            desc="Email hash enumeration",
            unit=" hashes",
            unit_scale=True,
            leave=False
        )
        result = self.hashes()
        if result:
            self.c.print(
                f"\nEmail found with hash enumeration after {self.n} hashes in {self.bar.format_interval(self.elapsed)} at {self.bar.format_sizeof(self.rate)} hashes/s:",
                style="#1e8cbe",
            )
            self.c.print(f"\t {result}", style="#1e8cbe bold")
        else:
            self.c.print("\n[red]Email not found with hash enumeration.[/red]")
        if self.public_emails:
            self.c.print(
                "\nPublic emails found on the Gravatar profile:", style="#1e8cbe"
            )
            for email in self.public_emails:
                hemail = self.hash_email(email)
                if result is None:
                    if hemail == self.hashed:
                        self.c.print(
                            f"\t [bold]{email}[/bold] (this is the primary Gravatar email - same hash)",
                            style="#1e8cbe",
                        )
                    else:
                        self.c.print(f"\t {email}", style="#1e8cbe bold")
                else:
                    if hemail != self.hashed:
                        self.c.print(f"\t {email}", style="#1e8cbe bold")

        show_profile = input("\nDo you want to display the profile info? (y/n):")
        if show_profile.lower() == "y":
            self.g.print_info()
        exit(0)
