from djangoaddicts.pygwalker.views import PygWalkerView, StaticCsvPygWalkerView
from tests.core.testapp.models import TestModel


class BasicPygWalkerView(PygWalkerView):
    queryset = TestModel.objects.all()


class ExplicitFieldsPygWalkerView(PygWalkerView):
    queryset = TestModel.objects.all()
    title = "TestModel Data Analysis"
    theme = "light"
    field_list = ["name"]


class CustomTemplatePygWalkerView(PygWalkerView):
    queryset = TestModel.objects.all()
    template_name = "testapp/my_custom_template.html"


class BasicStaticCsvPygWalkerViewView(StaticCsvPygWalkerView):
    csv_file = "tests/data/data.csv"


class CustomTemplateStaticCsvPygWalkerViewView(StaticCsvPygWalkerView):
    csv_file = "tests/data/data.csv"
    template_name = "testapp/my_custom_template.html"
