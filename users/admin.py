from django.contrib import admin
from users.models import Profile

# en este archivo se le indica al super admin que model puede usar.
# admin.site.register(Profile)

# Permite al admin ver el modelo y registrar


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ ModelAdmin = Encapsula todas las opciones de administrador
    y la funcionalidad de un modelo determinado."""

    """ las siguientes variables son propias de la clase modelAdmin
    y sus valores tienen que hacer referencia con los nombres de variable
     del modelo del que se hereda osea iguales"""
    list_display = (
        'user', 'phone', 'webpage'
    )
    list_editable = (
        'phone',
    )
    list_display_links = (
        'webpage', 'user'
    )
    list_filter = (
        'user__is_active',
    )
    search_fields = (
        'user__email', 'user'
    )
    fieldsets = (
        ('Usuario',  # Titulo
         {'fields': (
             ('user', 'webpage'),
             ('phone',)
         )}
         ),
        ('Otros',
         {'fields':(
             ('create',),
         )
          })
    )
    readonly_fields = ('create',)











