# test_MongoUserDict

from bson import ObjectId
from datetime import datetime
import mongo_objects
from pymongo.collection import Collection
import pytest
import secrets


@pytest.fixture(scope='session' )
def sampleData():
    return [
        {
            'name' : 'record 1',
            'amount' : 100,
        },
        {
            'name' : 'record 2',
            'amount' : 200,

        },
        {
            'name' : 'record 3',
            'amount' : 300,

        }
    ]


@pytest.fixture( scope='class' )
def getMPMUDClasses( mongo_db ):
    '''Return a set of PolymorphicMongoUserDict classes configured for a per-test-class unique collection'''

    class MyPolymorphicMongoUserDictBase( mongo_objects.PolymorphicMongoUserDict ):
        collection_name = secrets.token_hex(6)
        database = mongo_db

    class MyPolymorphicMongoUserDictA( MyPolymorphicMongoUserDictBase ):
        subclassKey = 'A'

    class MyPolymorphicMongoUserDictB( MyPolymorphicMongoUserDictBase ):
        subclassKey = 'B'

    class MyPolymorphicMongoUserDictC( MyPolymorphicMongoUserDictBase ):
        subclassKey = 'C'

    return ( MyPolymorphicMongoUserDictBase,
             MyPolymorphicMongoUserDictA,
             MyPolymorphicMongoUserDictB,
             MyPolymorphicMongoUserDictC )



@pytest.fixture( scope='class' )
def getPopulatedMPMUDClasses( getMPMUDClasses, sampleData ):

    (Base, A, B, C) = getMPMUDClasses

    # for each entry in the sampleData, save it as a separate polymorphic class
    a = A( sampleData[0] )
    a.save()
    b = B( sampleData[1] )
    b.save()
    c = C( sampleData[2] )
    c.save()

    return (Base, A, B, C)



class TestInitSubclass:
    '''Test __init_subclass__ permutations'''

    def test_init_subclass( self ):
        class MyTestClassBase( mongo_objects.PolymorphicMongoUserDict ):
            # create our own local testing namespace
            subclassMap = {}

        class MyTestSubclassA( MyTestClassBase ):
            subclassKey = 'A'

        class MyTestSubclassB( MyTestClassBase ):
            subclassKey = 'B'

        class MyTestSubclassC( MyTestClassBase ):
            pass

        # Verify that classes A and B were added to the map
        # Class C should be skipped because it doesn't have a non-None subclassKey
        assert MyTestClassBase.subclassMap == {
            'A' : MyTestSubclassA,
            'B' : MyTestSubclassB
        }

        # verify our local subclass map namespace didn't affect the module base class map
        assert len( mongo_objects.PolymorphicMongoUserDict.subclassMap ) == 0


    def test_init_subclass_duplicate_key( self ):
        with pytest.raises( Exception ):

            class MyTestClassBase( mongo_objects.PolymorphicMongoUserDict ):
                # create our own local testing namespace
                subclassMap = {}

            class MyTestSubclassA( MyTestClassBase ):
                subclassKey = 'A'

            class MyTestSubclassAnotherA( MyTestClassBase ):
                subclassKey = 'A'



class TestPolymorphicBasics:
    def test_subclassMap( self , getPopulatedMPMUDClasses ):
        '''getMPMUDClasses doesn't create a new subclassMap namespace
        Verify that our base class and the module base class subclassMaps are the same'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        assert len( Base.subclassMap ) == 3
        assert Base.subclassMap == mongo_objects.PolymorphicMongoUserDict.subclassMap


    def test_find_all( self, getPopulatedMPMUDClasses ):
        '''Verify all sample data are returned with the correct class'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        for obj in Base.find():
            # match the sample data to the expected classes
            if obj['name'] == 'record 1':
                assert obj['_sckey'] == 'A'
                assert isinstance( obj, A )
            elif obj['name'] == 'record 2':
                assert obj['_sckey'] == 'B'
                assert isinstance( obj, B )
            elif obj['name'] == 'record 3':
                assert obj['_sckey'] == 'C'
                assert isinstance( obj, C )
            else:
                assert False, 'unexpected sample data subclass'
            # since no project or flag was set, objects should not be readonly
            assert obj.readonly is False


    def test_find_single( self, getPopulatedMPMUDClasses ):
        '''Verify a single matching record is returned with the correct class'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        result = list( Base.find( { 'name' : 'record 1'} ) )
        assert len(result) == 1
        assert result[0]['_sckey'] == 'A'
        assert isinstance( result[0], A )


    def test_find_none( self, getPopulatedMPMUDClasses ):
        '''Verify a non-matching filter produces an empty result'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        result = list( Base.find( { 'not-a-match' : 'will not return data'} ) )
        assert len(result) == 0


    def test_find_projection_1( self, getPopulatedMPMUDClasses ):
        '''Verify "positive" projection works'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        for obj in Base.find( {}, { 'name' : True } ):
            assert '_id' in obj
            assert '_sckey' not in obj
            assert '_created' not in obj
            assert '_updated' not in obj
            assert 'name' in obj
            assert 'amount' not in obj
            assert obj.readonly is True


    def test_find_projection_2( self, getPopulatedMPMUDClasses ):
        '''Verify "positive" projection works while suppressing _id"'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        for obj in Base.find( {}, { '_id' : False, 'name' : True } ):
            assert '_id' not in obj
            assert '_sckey' not in obj
            assert '_created' not in obj
            assert '_updated' not in obj
            assert 'name' in obj
            assert 'amount' not in obj
            assert obj.readonly is True


    def test_find_projection_3( self, getPopulatedMPMUDClasses ):
        '''Verify "negative" projection works'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        for obj in Base.find( {}, { 'name' : False } ):
            assert '_id' in obj
            assert '_sckey' in obj
            assert '_created' in obj
            assert '_updated' in obj
            assert 'name' not in obj
            assert 'amount' in obj
            assert obj.readonly is True


    def test_find_projection_4( self, getPopulatedMPMUDClasses ):
        '''Verify "negative" projection works while suppressing _id'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        for obj in Base.find( {}, { '_id' : False, 'name' : False } ):
            assert '_id' not in obj
            assert '_sckey' in obj
            assert '_created' in obj
            assert '_updated' in obj
            assert 'name' not in obj
            assert 'amount' in obj
            assert obj.readonly is True


    def test_find_readonly( self, getPopulatedMPMUDClasses ):
        '''Verify find() readonly flag'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        for obj in Base.find( readonly=True ):
            assert obj.readonly is True


    def test_find_one( self, getPopulatedMPMUDClasses ):
        '''Verify a single sample document is returned with the correct class'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one()

        # match the sample data to the expected classes
        if obj['name'] == 'record 1':
            assert obj['_sckey'] == 'A'
            assert isinstance( obj, A )
        elif obj['name'] == 'record 2':
            assert obj['_sckey'] == 'B'
            assert isinstance( obj, B )
        elif obj['name'] == 'record 3':
            assert obj['_sckey'] == 'C'
            assert isinstance( obj, C )
        else:
            assert False, 'unexpected sample data subclass'

        # since no project or flag was set, objects should not be readonly
        assert obj.readonly is False


    def test_find_one_match( self, getPopulatedMPMUDClasses ):
        '''Verify a single matching record is returned with the correct class'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( { 'name' : 'record 1'} )
        assert obj is not None
        assert obj['_sckey'] == 'A'
        assert isinstance( obj, A )


    def test_find_one_none( self, getPopulatedMPMUDClasses ):
        '''Verify a non-matching filter produces a None result'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( { 'not-a-match' : 'will not return data'} )
        assert obj is None


    def test_find_one_projection_1( self, getPopulatedMPMUDClasses ):
        '''Verify "positive" projection works'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( {}, { 'name' : True } )
        assert '_id' in obj
        assert '_sckey' not in obj
        assert '_created' not in obj
        assert '_updated' not in obj
        assert 'name' in obj
        assert 'amount' not in obj
        assert obj.readonly is True


    def test_find_one_projection_2( self, getPopulatedMPMUDClasses ):
        '''Verify "positive" projection works while suppressing _id"'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( {}, { '_id' : False, 'name' : True } )
        assert '_id' not in obj
        assert '_sckey' not in obj
        assert '_created' not in obj
        assert '_updated' not in obj
        assert 'name' in obj
        assert 'amount' not in obj
        assert obj.readonly is True


    def test_find_one_projection_3( self, getPopulatedMPMUDClasses ):
        '''Verify "negative" projection works'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( {}, { 'name' : False } )
        assert '_id' in obj
        assert '_sckey' in obj
        assert '_created' in obj
        assert '_updated' in obj
        assert 'name' not in obj
        assert 'amount' in obj
        assert obj.readonly is True


    def test_find_one_projection_4( self, getPopulatedMPMUDClasses ):
        '''Verify "negative" projection works while suppressing _id'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( {}, { '_id' : False, 'name' : False } )
        assert '_id' not in obj
        assert '_sckey' in obj
        assert '_created' in obj
        assert '_updated' in obj
        assert 'name' not in obj
        assert 'amount' in obj
        assert obj.readonly is True


    def test_find_one_readonly( self, getPopulatedMPMUDClasses ):
        '''Verify find_one() readonly flag'''
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.find_one( readonly=True )
        assert obj.readonly is True


    def test_instantiate( self, getPopulatedMPMUDClasses ):
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.instantiate( { '_sckey' : 'A' } )
        assert isinstance( obj, A )
        assert obj.readonly is False


    def test_getSubclassByKey( self, getMPMUDClasses ):
        (Base, A, B, C) = getMPMUDClasses
        assert Base.getSubclassByKey( 'A' ) == A


    def test_getSubclassFromDoc( self, getMPMUDClasses ):
        (Base, A, B, C) = getMPMUDClasses
        assert Base.getSubclassFromDoc( { Base.subclassKeyName : 'A' } ) == A


    def test_instantiate_readonly( self, getPopulatedMPMUDClasses ):
        (Base, A, B, C) = getPopulatedMPMUDClasses
        obj = Base.instantiate( { '_sckey' : 'B' }, readonly=True )
        assert isinstance( obj, B )
        assert obj.readonly is True


    def test_loadProxyById( self, getPopulatedMPMUDClasses ):
        '''Verify find_one() readonly flag'''
        (Base, A, B, C) = getPopulatedMPMUDClasses

        # loop through sample objects
        for source in Base.find():

            # load the same object with an empty proxy tree
            result = Base.loadProxyById( source.id() )

            # verify that the type of the object is correct
            assert type(source) == type(result)

            # verify the objects are the same
            assert source == result

            # verify the object is readonly
            assert result.readonly is False


    def test_loadProxyById( self, getPopulatedMPMUDClasses ):
        '''Verify find_one() readonly flag'''
        (Base, A, B, C) = getPopulatedMPMUDClasses

        # loop through sample objects
        for source in Base.find():

            # load the same object with an empty proxy tree
            result = Base.loadProxyById( source.id(), readonly=True )

            # verify that the type of the object is correct
            assert type(source) == type(result)

            # verify the objects are the same
            assert source == result

            # verify the object is readonly
            assert result.readonly is True





