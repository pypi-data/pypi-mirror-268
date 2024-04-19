# WARNING - Do not add import * in this module
from pyspark import Row
from pyspark.sql import SparkSession
from functools import lru_cache

class ConfigBase:

    class SecretValue:
        def __init__(self, prophecy_spark=None, secretScope: str="", secretKey: str="", providerType: str="Databricks", **kwargs):
            self.prophecy_spark = prophecy_spark
            self.secretScope = secretScope
            self.secretKey = secretKey
            self.providerType = providerType

        def __deepcopy__(self, memo):
            import copy
            from pyspark.sql import SparkSession
            cls = self.__class__
            result = cls.__new__(cls)
            memo[id(self)] = result
            for k, v in self.__dict__.items():
                if isinstance(v, SparkSession):
                    setattr(result, k, v)
                else:
                    setattr(result, k, copy.deepcopy(v, memo))
            return result

        @lru_cache()
        def __str__(self):
            if (self.prophecy_spark is not None and self.prophecy_spark.sparkContext.getConf().get("prophecy.schema.analysis") == "True"):
                return f"{self.secretScope}:{self.secretKey}"
            self.jvm = self.prophecy_spark.sparkContext._jvm
            self.secret_manager = self.jvm.io.prophecy.libs.secrets.ProphecySecrets
            return self.secret_manager.get(self.secretScope, self.secretKey, self.providerType)

    def updateSpark(self, spark):
        self.spark = spark

    def get_dbutils(self, spark):
        try:
            dbutils  # Databricks provides an instance of dbutils be default. Checking for it's existence
            return dbutils
        except NameError:
            try:
                from pyspark.dbutils import DBUtils

                _dbutils = DBUtils(spark)
            except:
                try:
                    import IPython

                    _dbutils = IPython.get_ipython().user_ns["dbutils"]
                except Exception as e:
                    from prophecy.test.utils import ProphecyDBUtil

                    _dbutils = ProphecyDBUtil

            return _dbutils

    def get_int_value(self, value):
        if value is not None:
            return int(value)
        else:
            return value

    def get_float_value(self, value):
        if value is not None:
            return float(value)
        else:
            return value

    def get_bool_value(self, value):
        if value is not None:
            return bool(value)
        else:
            return value

    # Old function, keeping it for backward compatibility
    def generate_object(self, value, cls):
        if isinstance(value, list):
            return [self.generate_object(x, cls) for x in value]
        elif isinstance(value, dict):
            return cls(**value)
        return value

    # Old function, keeping it for backward compatibility
    def get_object(self, default, override, cls):
        if override == None:
            return default
        else:
            return self.generate_object(override, cls)

    def generate_config_object(self, spark, value, cls):
        if isinstance(value, list):
            return [self.generate_config_object(spark, x, cls) for x in value]
        elif isinstance(value, dict):
            return cls(**{**{"prophecy_spark": spark}, **value})
        return value

    def get_secret_config_object(self, spark, default, override, cls):
        if isinstance(override, str) and override.count(":") == 1:
            parts = override.split(":")
            values = {"providerType": "Databricks", "secretScope": parts[0], "secretKey": parts[1]}
            return self.get_config_object(spark, default, values, cls)
        else:
            return self.get_config_object(spark, default, override, cls)

    def get_config_object(self, spark, default, override, cls):
        if override == None:
            return default
        else:
            return self.generate_config_object(spark, override, cls)

    def to_dict(self):
        def to_dict_recursive(obj):
            def should_include(key, value):
                # remove any unwanted objects from the config:
                return key not in ["spark", "prophecy_spark"] and not isinstance(value, SparkSession)
            if isinstance(obj, (list, tuple)):
                return [to_dict_recursive(item) for item in obj]
            elif isinstance(obj, dict):
                return {key: to_dict_recursive(value) for key, value in obj.items() if should_include(key, value)}
            elif hasattr(obj, "__dict__"):
                return to_dict_recursive({key: value for key, value in obj.__dict__.items() if should_include(key, value)})
            elif hasattr(obj, "__slots__"):
                return to_dict_recursive({slot: getattr(obj, slot) for slot in obj.__slots__ if should_include(slot, getattr(obj, slot))})
            else:
                return obj
        return to_dict_recursive(self)

    def update_from_row(self, row: Row):
        import copy
        new_config = copy.deepcopy(self)
        spark_variable = None
        updated_config_json = {**new_config.to_dict(), **row.asDict(recursive=True)}
        if hasattr(new_config, "spark") and new_config.spark is not None:
            spark_variable = new_config.spark
        elif hasattr(new_config, "prophecy_spark") and new_config.prophecy_spark is not None:
            spark_variable = new_config.spark
        return self.get_config_object(spark_variable, new_config, updated_config_json, new_config.__class__)

    def update_from_row_map(self, row: Row, config_to_column: dict):
        import copy
        new_config = copy.deepcopy(self)
        spark_variable = None
        row_as_dict = row.asDict(recursive=True)
        overridden_values = {}
        for config_name, column_name in config_to_column.items():
            overridden_values[config_name] = row_as_dict[column_name]
        updated_config_json = {**new_config.to_dict(), **overridden_values}
        if hasattr(new_config, "spark") and new_config.spark is not None:
            spark_variable = new_config.spark
        elif hasattr(new_config, "prophecy_spark") and new_config.prophecy_spark is not None:
            spark_variable = new_config.spark
        return self.get_config_object(spark_variable, new_config, updated_config_json, new_config.__class__)

    def __deepcopy__(self, memo):
        import copy
        from pyspark.sql import SparkSession
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if isinstance(v, SparkSession):
                setattr(result, k, v)
            else:
                setattr(result, k, copy.deepcopy(v, memo))
        return result
