# Databricks notebook source
# MAGIC %run ./_utility-methods

# COMMAND ----------

DA = DBAcademyHelper()
# Don't clean up, continue where we left off.
# DA.cleanup()
DA.init(create_db=False)
DA.conclude_setup()

