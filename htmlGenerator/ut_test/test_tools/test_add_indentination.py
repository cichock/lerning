import unittest
from tools.add_indents import Formater
import templates.Registration_Form as form_template
import Html_Tags as tags


def html_with_children():
    return '''<html>
    <head>
        <title>new title</title>
    </head>
    <body>
        <div class="container">
            <h1>Header</h1>
        </div>
    </body>
</html>'''


def registration_form():
    return '''<form class="p-2">
    <div class="form-group">
        <label>Name:</label>
        <input placeholder="Type your name" class="form-control">
    </div>
    <div class="form-group">
        <label>Surname:</label>
        <input placeholder="Type your surname" class="form-control">
    </div>
    <div class="form-group">
        <label>Email:</label>
        <input placeholder="Type your email" class="form-control">
    </div>
    <div class="form-group">
        <label>Password:</label>
        <input placeholder="Type your pasword" class="form-control mb-1">
        <input placeholder="Repeat pasword" class="form-control mt-1">
    </div>
    <button class="btn btn-dark">Register</button>
</form>'''


def invalid_html():
    return '''<html>
<head>
<title>new title
</hea
<body>
<div class="container">
<h1>Header</h1>
</div>
</body>
</html>'''


class Test_add_indentination(unittest.TestCase):


    def setUp(self):
        self.formater = Formater()
        self.sut = tags.html()


    def test_align_html(self):
        self.sut.head()

        expect_head = '<head></head>'
        expect_html = f'<html>\n    {expect_head}\n</html>'
        self.assertEqual(self.formater.format_indents(self.sut.html()), expect_html)
        self.assertEqual(self.sut.format_html(), expect_html)


    def test_align_html_with_children(self):
        self.sut.head().title('new title')
        self.sut.body().div().add_class("container")
        self.sut.body().div().h1('Header')

        self.assertEqual(self.formater.format_indents(self.sut.html()), html_with_children())
        self.assertEqual(self.sut.format_html(), html_with_children())


    def test_align_registration_form(self):
        form = form_template.Registration_Form()
        self.assertEqual(self.formater.format_indents(form.html()), registration_form())
        self.assertEqual(form.format_html(), registration_form())


    def test_align_invalid_html(self):
        self.assertEqual(self.formater.format_indents(invalid_html()), invalid_html())