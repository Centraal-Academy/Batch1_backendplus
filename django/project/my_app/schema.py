from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from . import models

class Person(DjangoObjectType):
    class Meta:
        model = models.Person
        filter_fields = {
            'name' : ["exact",'icontains'],
            'email' : ["icontains", 'iendswith'],
            'program__name' : ["icontains",],
        }
        interfaces = (graphene.relay.Node,)

class Program(DjangoObjectType):
    class Meta:
        model = models.Program
        filter_fields = ['name', 'instructor']
        interfaces = (graphene.relay.Node,)

class CreateProgram(graphene.Mutation):
    class Input:
        name = graphene.String()
        instructor = graphene.String()

    program = graphene.Field(Program)

    def mutate(self, info, name, instructor):
        new_program = models.Program(
                                name = name,
                                instructor = instructor
                                )
        new_program.save()
        return CreateProgram(program=new_program)

class CreatePerson(graphene.Mutation):
    class Input:
        name = graphene.String()
        email = graphene.String()
        age = graphene.Int()
        program = graphene.Int()

    person = graphene.Field(Person)

    def mutate(self, info, **kwargs):
        new_person = models.Person()
        new_person.name = kwargs.get('name')
        new_person.email = kwargs.get('email')
        new_person.age = kwargs.get('age')
        new_person.program = models.Program.objects.get(pk=kwargs.get('program'))
        new_person.save()
        return CreatePerson(person=new_person)


class Mutation(graphene.ObjectType):
    create_program = CreateProgram.Field()
    create_person = CreatePerson.Field()

class Query(graphene.ObjectType):
    person = graphene.relay.Node.Field(Person)
    all_people = DjangoFilterConnectionField(Person)

    program = graphene.relay.Node.Field(Program)
    all_programs = DjangoFilterConnectionField(Program)
    program_list = graphene.List(Program)

    def resolve_program_list(self, info, **kwargs):
        return models.Program.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)