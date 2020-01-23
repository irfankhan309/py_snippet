class InitialSignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget = forms.PasswordInput)
    password_repeat = forms.CharField(max_length=255, widget = forms.PasswordInput)
    
    def clean_message(self):
        email = self.clean_data.get('email', '')
        password = self.clean_data.get('password', '')
        password_repeat = self.clean_data.get('password_repeat', '')

        try:
            User.objects.get(email_address = email)
            raise forms.ValidationError("Email taken.")
        except User.DoesNotExist:
            pass

        if password != password_repeat:
            raise forms.ValidationError("The passwords don't match.")