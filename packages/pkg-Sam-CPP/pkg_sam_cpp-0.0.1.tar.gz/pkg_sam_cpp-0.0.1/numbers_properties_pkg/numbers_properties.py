# feedback_counter/feedback_counter/counter.py

from django.apps import apps

class FeedbackCounter:
    @staticmethod
    def count_titles(app_name, model_name):
        Feedback = apps.get_model(app_name, model_name)
        title_count = Feedback.objects.count()
        return title_count
