# from django.dispatch import receiver
# from django.db.models import signals
# from user.models import User
# from versatileimagefield.image_warmer import VersatileImageFieldWarmer

# @receiver(signals.post_save, sender=User)
# def warm_user_images(sender, instance, **kwargs):
#     warmer = VersatileImageFieldWarmer(
#         instance_or_queryset = instance,
#         rendition_key_set = 'profile_picture',
#         image_attr = 'profile_picture'
#     )

#     if instance.profile_picture:
#         num_created, failed_to_create = warmer.warm()
#     else:
#         return


# @receiver(signals.post_delete, sender=User)
# def delete_images(sender, instance, **kwargs):
#     '''Delete all the related images of a user on deletion.'''
#     instance.profile_picture.delete_all_created_images()
#     instance.profile_picture.delete(save=False)

