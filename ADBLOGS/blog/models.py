from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# class Reporter(models.Model):
#     full_name = models.CharField(max_length=80)
#     def __str__(self):
#         return self.full_name
class Article(models.Model):
    # pub_date = models.DateField(auto_now_add=True)
    pub_date = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
    # from blog.models import Article,Reporter
    # Reporter.objects.get(id=1)
    # Article.objects.create(headline='In pictures: Russia invades Ukraine',content="Russia had been tightening its military grip around Ukraine since last year, amassing tens of thousands of soldiers, as well as equipment and artillery, on its neighbor's doorstep. The escalation in the years-long conflict has triggered the greatest security crisis in Europe since the Cold War, and it has also sparked an intense showdown between Western powers and Moscow.Editor's note: This gallery contains graphic images. Viewer discretion is advised.",r)

