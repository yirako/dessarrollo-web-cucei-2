from django.db import models
from django.forms import ModelForm, PasswordInput

# Create your models here.
class Usuario(models.Model):
    codigo = models.CharField(max_length=32, unique=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    passw = models.CharField(max_length=32)
    email = models.EmailField()
    pagweb = models.URLField(blank=True,  null=True)

    def __unicode__(self):
        return "%r: %r" %(self.codigo, self.nombre)

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['codigo', 'nombre', 'edad', 'passw', 'email', 'pagweb']
        widgets = {
            'passw': PasswordInput,
        }