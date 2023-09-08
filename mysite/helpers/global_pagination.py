from django.http import JsonResponse  , request

from django.conf import settings
import logging 

logger = logging.getLogger(__name__)




class GlobalPagination():
    query_set = None
    try:
        page_size = settings.GLOBAL_PAGINATION.get('PAGE_SIZE')
    except AttributeError as e:
        page_size = 2 
        logger.warn('Page size is not set in global settings, taking 2 as default')
 

    
    @staticmethod
    def get_current_page_num(request : request):
            
        page_num =  request.GET.get('page_num')
        if page_num is None: 
            return 1
        return int(page_num)
    

    
    def calculate_page_indices(self , page_num : int ):

        if page_num  < 1: 
            page_num = 1
        
        
        start_index  =  (page_num  -1) * self.page_size
        end_index =  start_index + self.page_size


        return start_index , end_index




                               
    @classmethod
    def as_view(cls, request: request):
        page_num = cls.get_current_page_num(request)

        s_at , e_at =  cls.calculate_page_indices(cls , page_num=page_num)
       

        
        posts_res = list(cls.query_set[s_at : e_at].values())
    

        return JsonResponse({
            "results": posts_res,
            "page_num": page_num,
            "page_size" :  cls.page_size
        })



        

