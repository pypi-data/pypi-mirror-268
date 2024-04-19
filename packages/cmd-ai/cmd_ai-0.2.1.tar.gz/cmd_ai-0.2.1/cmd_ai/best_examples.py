#!/usr/bin/env python3

from fire import Fire
from console import fg,bg
BEST = f"""
{fg.yellow}# TOOLS: u {fg.default}
cmd_ai  "Pocasi zitra ve Stredoceskem kraji: jaka bude nejvyssi teplota?" -u
cmd_ai  "Pocasi zitra ve Stredoceskem kraji, ne na zapade, jihu, severu, vychode: bude prset?" -u
cmd_ai  "Pocasi zitra ve Stredoceskem kraji, ne na zapade, jihu, severu, vychode: bude prset? Velmi strucne!" -u --csspeak
{fg.yellow}# COMMIT commads{fg.default}
git diff | cmd_ai "Create oneliner git commit command with -a -m parameters "
"""
def main():
    print(BEST)

if __name__=="__main__":
    Fire(main)
