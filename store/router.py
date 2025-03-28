class HeartDataRouter:
    """
    Router to control all database operations on models in the heart application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read heart models go to heart_data database.
        """
        if model._meta.app_label == 'store' and model._meta.model_name == 'patient':
            return 'heart_data'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Writes to heart models go to heart_data database.
        """
        if model._meta.app_label == 'store' and model._meta.model_name == 'patient':
            return 'heart_data'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the heart app is involved.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the heart app only appears in the 'heart_data' database.
        """
        if app_label == 'store' and model_name == 'patient':
            return db == 'heart_data'
        return db == 'default'