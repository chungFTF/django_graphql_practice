import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")     


class Query(graphene.ObjectType):

    one_quiz = graphene.Field(QuizzesType, id=graphene.Int())
    def resolve_one_quiz(self, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_quiz(self, info):
        return "This is !"


    all_quizzes = DjangoListField(QuizzesType)
    
    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    
    all_category = DjangoListField(CategoryType)

    def resolve_all_category(root, info):
        return Category.objects.all()
    
    one_question = graphene.Field(QuestionType, id=graphene.Int())
    def resolve_one_question(self, info, id):
        return Question.objects.get(pk=id)
    
    one_answer = graphene.List(AnswerType, id=graphene.Int())
    def resolve_one_answer(self, info, id):
        return Answer.objects.filter(question=id)


schema = graphene.Schema(query=Query) 