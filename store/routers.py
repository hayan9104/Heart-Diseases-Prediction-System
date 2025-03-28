# store/routers.py

class StoreRouter:
    """
    A router to control all database operations on models in the
    store application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read store models go to heart_save_data.
        """
        if model._meta.app_label == 'store':
            return 'heart_save_data'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write store models go to heart_save_data.
        """
        if model._meta.app_label == 'store':
            return 'heart_save_data'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the store is involved.
        """
        if obj1._meta.app_label == 'store' or \
           obj2._meta.app_label == 'store':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the store only appears in the 'heart_save_data'
        database.
        """
        if app_label == 'store':
            return db == 'heart_save_data'
        return None