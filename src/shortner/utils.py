import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size)
    root_class = instance.__class__
    qs = root_class.objects.filter(shortcode=new_code).exists()
    if qs:
        return create_shortcode(size)
    return new_code
