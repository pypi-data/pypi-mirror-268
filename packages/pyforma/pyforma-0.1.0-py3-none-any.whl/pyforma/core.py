# dataclass_forms/__init__.py
from typing import Any, Type
from dataclasses import fields
from jinja2 import Template

class Form:
    def __init__(self, model_class: Type[Any]) -> None:
        self.model_class = model_class
    
    def to_dict(self) -> dict:
        fields_dict = {}
        for field in fields(self.model_class):
            field_name = field.name
            field_type = field.type.__name__
            fields_dict[field_name] = field_type
        return fields_dict

    @staticmethod
    def generate_form(model_class: Type[Any]) -> Template:
        template_str = """
        <form>
            {% for field in form_fields %}
            <label>{{ field.name }}</label><br>
            {% if field.type.__name__ == 'text' %}
            <input type="text" name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}><br>
            {% elif field.type.__name__ == 'textarea' %}
            <textarea name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}></textarea><br>
            {% elif field.type.__name__ == 'number' %}
            <input type="number" name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}><br>
            {% elif field.type.__name__ == 'checkbox' %}
            <input type="checkbox" name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}><br>
            {% elif field.type.__name__ == 'date' %}
            <input type="date" name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}><br>
            {% elif field.type.__name__ == 'datetime' %}
            <input type="datetime-local" name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}><br>
            {% elif field.type.__name__ == 'picklist' %}
            <select name="{{ field.name }}" {% if field.metadata.get('required') %} required {% endif %}>
                {% if field.default_factory != '_MISSING_TYPE' %}
                    {% for item in field.default_factory %}
                    <option value="{{ item }}">{{ item }}</option>
                    {% endfor %}
                {% endif %}
            </select><br>
            {% else %}
            <!-- Handle other data types as needed -->
            {% endif %}
            {% endfor %}
            <input type="submit" value="Submit">
        </form>
        """
        return Template(template_str)

    def render_form(self) -> str:
        form_template = self.generate_form(self.model_class)
        rendered_form = form_template.render(form_fields=fields(self.model_class))
        return rendered_form
    
    def save_html(self, filename: str) -> None:
        form_html = self.render_form()
        with open(filename, 'w') as f:
            f.write(form_html)
