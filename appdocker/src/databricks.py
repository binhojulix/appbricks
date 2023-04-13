from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi
import os


class Token:

    @staticmethod
    def api_client(): 
      return ApiClient(
        host  = os.getenv('DATABRICKS_HOST'),
        token = os.getenv('DATABRICKS_TOKEN') )


    def lista_cluster(self):
      api_client     = Token.api_client()
      clusters_api   = ClusterApi(api_client)
      clusters_list  = clusters_api.list_clusters()
      return {
              'elements': [Token.to_json(elemento) for elemento in clusters_list ]
          }


      @staticmethod
      def to_json(cluster):
        return {
          'cluser_name' : cluster['cluster_name'],
          'cluster_id'  :  cluster['cluster_id']
        }

