from .models import Video

#sender=Welche Instanz, instance=, created=True sobald erstellt, 
def video_post_save(sender, instance, created, **kwargs):
    print('Video wurde gespeichert')
    if created:
      print('Video wurde erschaffen')