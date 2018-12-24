# -*- coding: utf-8

# Run: python manage.py shell < init_db_script.py

from animationfinder.models import Item, Animation, Description, Synonym

for i in range(10):
    Item.objects.create()
    Animation.objects.create()
    Description.objects.create()

# Creating synonyms for sentence "We saw her duck. She loves ducks."

Synonym.objects.create(name="we")
Synonym.objects.create(name="saw")
Synonym.objects.create(name="her")
Synonym.objects.create(name="duck")
Synonym.objects.create(name="she")
Synonym.objects.create(name="loves")
Synonym.objects.create(name="ducks")

