from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv()


class DataBricksProp:

    @staticmethod
    def api_client(): 

      host =  os.getenv('DATABRICKS_HOST')
      token =  os.getenv('DATABRICKS_TOKEN')
      return ApiClient(
        host  = host,
        token = token )


    def lista_cluster(self):
      api_client     = DataBricksProp.api_client()
      clusters_api   = ClusterApi(api_client)
      clusters_list  = clusters_api.list_clusters()
      return {
              'elements': [DataBricksProp.to_json(elemento) for elemento in clusters_list ]
          }


      @staticmethod
      def to_json(cluster):
        return {
          'cluser_name' : cluster['cluster_name'],
          'cluster_id'  :  cluster['cluster_id']
        }

