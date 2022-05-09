from rest_framework import serializers
from versatileimagefield.utils import get_url_from_image_key



class ImageKeySerializer(serializers.ImageField):
    def __init__(self, key, *args, **kwargs):
        self.key = key
        kwargs['read_only'] = True
        super().__init__(*args, **kwargs)

    def get(self, value, key_name, request):
        
        print(f'\nKey Name: {key_name}\n')
        print(f'\nValue: {value}\n')
        print(f'\nRequest: {request}\n')


        try:
            key = value.instance.SIZES[value.field.name][key_name]
            print(f'\nKey: {key}\n')

        except KeyError:    
            return
        # except AttributeError:
        #     key = value
        url = get_url_from_image_key(value, key)
        print(f'\nUrl: {url}\n')
        # url = url.replace('%2520', '%20')

        if '%2520' in url:
            return None

        if request:
            print(f'\nAbsolute Uri: {request.build_absolute_uri(url)}\n')
            return request.build_absolute_uri(url)
        else:
            try:
                rep = super().to_representation(url)
                print(f'\nRep: {rep}\n')
                if rep is None:
                    return url
                return rep
            except AttributeError:
                return super().to_native(url)

    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get('request', None)
        if type(self.key) == str:
            return self.get(value, self.key, request)
        elif type(self.key) == list:
            urls = {}
            for key_name in self.key:
                urls[key_name] = self.get(value, key_name, request)
            return urls
        else:
            raise ValueError('Key must be either string or a list.')

    to_native = to_representation