
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

## validators=[UniqueValidator(queryset=User.objects.all())

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only = True,
        required=True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )

    password2 = serializers.CharField(
        write_only = True,
        required=True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )

    def create(self, validated_data):
        ## password row olarak gitmez db ye
        password = validated_data.pop("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password" : "Password didn't match..."}
            )

        return data




    # email kullanim neden 
    #ilgili alanı frontend'ten bağımsız olarak direk backend database tarafında zorunlu kılmak için, doğrumudur hocam?
    #  hem unique hem de required olmasi icin
    # write_only sadece post yada put 
    #password için requiredın defaultu True olduğu için yazılmasada oluyor

