from django import forms
from .models import Product

# Список запрещенных слов
FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

    # Валидация для названия
    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise forms.ValidationError(f"Название не может содержать слово: {word}")
        return name

    # Валидация для описания
    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise forms.ValidationError(f"Описание не может содержать слово: {word}")
        return description

    # Кастомная валидация для поля price
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    # Стилизация формы
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Добавление класса для стилизации
    