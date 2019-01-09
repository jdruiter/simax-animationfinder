# -*- coding: utf-8

"""
Run:

python manage.py shell < init_db_script.py
"""

from animationfinder.models import Animation, Synonym

# Creating synonyms for sentence "We saw her duck. She loves ducks."
s1 = Synonym.objects.create(name="we", description="we (multiple persons)")
s2 = Synonym.objects.create(name="saw", description="saw (past of seeing)")
s3 = Synonym.objects.create(name="her", description="her (female)")
s4 = Synonym.objects.create(name="duck", description="duck (going down)")
s5 = Synonym.objects.create(name="duck", description="duck (the animal)")
s6 = Synonym.objects.create(name="she", description="she (female, singular)")
s7 = Synonym.objects.create(name="loves", description="loves (to like someone/something)")
s8 = Synonym.objects.create(name="ducks", description="ducks (duck, animal, multiple)")

# Creating Animations for sentence "We saw her duck. She loves ducks."
s1.animations.create(name="we")
s2.animations.create(name="saw")
s3.animations.create(name="her")
s4.animations.create(name="duck")
s5.animations.create(name="duck")
s6.animations.create(name="she")
s7.animations.create(name="loves")
s8.animations.create(name="ducks")

print "done"
