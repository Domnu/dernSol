import re


def test_regex(pattern, text):
    match = re.search(pattern, text)
    if match:
        print("Match trouvé :", match.group())
    else:
        print("Aucun match trouvé.")


# Exemples d'utilisation
test_regex(r'[A-Za-z0-9.-]+', 'exemple@email.com')
test_regex(r'[A-Za-z0-9.-]+', '123-456-7890')
test_regex(r'[A-Za-z0-9.-]+', 'adresse_postale')
test_regex(r'[A-Za-z0-9.-]+', '!@#$%^&*()')

# Exemples d'utilisation pour les noms et prénoms francophones
print('\nLin 19  - Regex pour noms et prénoms en fr.=')
test_regex(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+([- \'][A-Za-zÀ-ÖØ-öø-ÿ]+)*$', 'Jean-François')
test_regex(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+([- \'][A-Za-z0-9À-ÖØ-öø-ÿ]+)*$', 'Jean-François 210')
test_regex(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+([- \'][A-Za-zÀ-ÖØ-öø-ÿ]+)*$', "Marie-Claire d'Arcy")
test_regex(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+([- \'][A-Za-z0-9À-ÖØ-öø-ÿ]+)*$', 'Léa 150')
test_regex(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+([- \'][A-Za-zÀ-ÖØ-öø-ÿ]+)*$', '123abc')