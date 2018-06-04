rowsPerPage = 5

from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import DjangoBoard

def home(request):
    
    boardList = DjangoBoard.objects.order_by('-id')[0:5]
    current_page = 1
    totalCnt = DjangoBoard.objects.all().count()
    
    pagingHelperlns = pagingHelper();
    totalPageList = pagingHelperlns.getTotalPageList(totalCnt, rowsPerPage)
    print ('totalPageList', totalPageList)

    return render_to_response('listSpecificPage.html',{'boardList':boardList, 'totalCnt':totalCnt, 'current_page':current_page, 'totalPageList':totalPageList})
##################################################################################################
def viewWork(request):
    pk= request.GET['memo_id']
    boardData = DjangoBoard.objects.get(id=pk)
    
    DjangoBoard.objects.filter(id=pk).update(hits = boardData.hits + 1)
    
    return render_to_response('viewMemo.html', {'memo_id': request.GET['memo_id'],
                                                'current_page':request.GET['current_page'],
                                                'searchStr': request.GET['searchStr'],
                                                'boardData': boardData } )

####################################################3
def show_write_form(request):
    return render_to_response('writeBoard.html')

def DoWriteBoard(request):
    br = DjangoBoard (subject = request.POST['subject'],
                      name = request.POST['name'],
                      mail = request.POST['email'],
                      memo = request.POST['memo'],
                      created_date = timezone.now(),
                      hits = 0
                     )
    br.save()
    
def listSpecificPageWork(request):
    current_page = request.GET['current_page']
    totalCnt = DjangoBoard.objects.all().count()

    print ('current_page=', current_page)
    
    boardList = DjangoBoard.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil( rownum / %s ) as page FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS \ FROM SAMPLE_BOARD_DJANGOBOARD ORDER BY ID DESC) X) Z WHER page = %s', [rowsPerPage, current_page])
    
    print ('boardList=',boardList, 'count()=', totalCnt)
    
    pagingHelperlns = pagingHelper();
    totalPageList = pagingHelperlns.getTotalPageList( totalCnt, rowsPerPage)
    print ('totalPageList', totalPageList)
    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,'current_page':int(current_page),'totalPageList':totalPageList} )
# Create your views here.

###################################################
class pagingHelper:
    
    def getTotalPageList(self, total_cnt, rowsPerPage):
        if ((total_cnt % rowsPerPage)==0):
            self.total_pages = total_cnt / rowsPerPage;
            print ('getTotalPage #1')
        else:
            self.total_pages = (total_cnt / rowsPerPage) + 1;
            print('getTotalPage #2')
            
        self.totalPageList = []
        for i in range(int(float(self.total_pages))):
            self.totalPageList.append(i+1)
            
        return self.totalPageList
    
    def __init__(self):  
        self.total_pages = 0
        self.totalPageList = 0
##########################################        


    