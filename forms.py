from django import forms
from .models import Usuario, Endereco


class LoginForm(forms.Form):
 
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@dominio.com'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'bairro', 'localidade', 'uf', 'numero', 'complemento']
        widgets = {
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 57000-000',
                'onkeyup': 'buscarCep(this.value)'
            }),
            'rua': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua',
                'readonly': 'readonly'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro',
                'readonly': 'readonly'
            }),
            'localidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade',
                'readonly': 'readonly'
            }),
            'uf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UF',
                'readonly': 'readonly'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apto, Bloco, etc.'
            }),
        }


class CadastroUsuarioForm(forms.ModelForm):
    
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail principal'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mínimo de 8 caracteres'})
    )
    password_confirm = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita a senha'}),
        max_length=128
    )

    class Meta:
        model = Usuario
       
        fields = ['nome_completo', 'idade', 'tipo_deficiencia', 'email', 'password']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome Completo'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'tipo_deficiencia': forms.Select(attrs={'class': 'form-control'})
        }
    
 
    username = forms.CharField(widget=forms.HiddenInput(), required=False)


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        email = cleaned_data.get("email")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError(
                "As senhas não coincidem!"
            )
        
       
        if email:
            cleaned_data['username'] = email
        
        return cleaned_data