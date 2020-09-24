from django.test import TestCase
from .models import Word, Definition

class SetUp(TestCase):
    def setUp(self):
        self.w1 = Word.objects.create(name="house")
        self.d11 = Definition.objects.create(description="place where you live", word=self.w1)
        self.w1.save()
        self.d11.save()
        
    def tearDown(self):
        Word.objects.all().delete()
        Definition.objects.all().delete()  

class ViewsTestCase(SetUp):
    def test_delete(self):
        # Get an existing word
        w = Word.objects.filter(name='house').first()
        # Check that exists in the dictionary
        self.assertNotEqual(w, None)
        # Remove it
        self.client.get('/delete/house')
        # Get the word again
        w = Word.objects.filter(name='house').first()
        # Check that the word does not exist any more in the dictionary
        self.assertEqual(w, None)
        
    def test_insert(self):
        # Check that 'car' does not exist in the dictionary
        w = Word.objects.filter(name='car').first()        
        self.assertEqual(w, None)
        self.client.post('/add', {'name' : 'car',
                                  'definition_set-TOTAL_FORMS': '3',
                                  'definition_set-INITIAL_FORMS': '0',
                                  'definition_set-MIN_NUM_FORMS': '0',
                                  'definition_set-MAX_NUM_FORMS': '1000',
                                  'definition_set-0-description': 'small vehicle'})
        # Check that 'car' exists in the dictionary with its definition                         
        w = Word.objects.filter(name='car').first()        
        self.assertNotEqual(w, None)
        definition = w.definition_set.first()
        self.assertEqual(definition.description, 'small vehicle')
    
    def test_edit_description(self):
        # Check that 'house' exists with its definition
        w = Word.objects.filter(name='house').first()        
        self.assertNotEqual(w, None)
        definition = w.definition_set.first()
        self.assertEqual(definition.description, 'place where you live')
        # Edit 'house' description
        self.client.post('/edit/house', {'name' : 'house',
                                         'definition_set-TOTAL_FORMS': '4',
                                         'definition_set-INITIAL_FORMS': '1',
                                         'definition_set-MIN_NUM_FORMS': '0',
                                         'definition_set-MAX_NUM_FORMS': '1000',
                                         'definition_set-0-description': 'place to live',
                                         'definition_set-0-id': definition.id,
                                         'definition_set-0-word': w.id})
        # Check that definition has been changed
        w = Word.objects.filter(name='house').first()        
        self.assertNotEqual(w, None)
        definition = w.definition_set.first()
        self.assertEqual(definition.description, 'place to live')
        
    def test_edit_name(self):
        # Check that 'house' exists with its definition
        w = Word.objects.filter(name='house').first()        
        self.assertNotEqual(w, None)
        definition = w.definition_set.first()
        self.assertEqual(definition.description, 'place where you live')
        # Edit 'house'
        self.client.post('/edit/house', {'name' : 'home',
                                         'definition_set-TOTAL_FORMS': '4',
                                         'definition_set-INITIAL_FORMS': '1',
                                         'definition_set-MIN_NUM_FORMS': '0',
                                         'definition_set-MAX_NUM_FORMS': '1000',
                                         'definition_set-0-description': 'place where you live',
                                         'definition_set-0-id': definition.id,
                                         'definition_set-0-word': w.id})
        # Check that name has been changed
        w = Word.objects.filter(name='house').first()        
        self.assertEqual(w, None)
        w = Word.objects.filter(name='home').first()        
        self.assertNotEqual(w, None)
        definition = w.definition_set.first()
        self.assertEqual(definition.description, 'place where you live')
        
        
        
        
        
        