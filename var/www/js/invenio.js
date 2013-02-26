$(document).ready(function() {

  /*
   * sorting
   */
  var domain = 'https://' + document.domain + '/';
  $('body.home .narrowsearchbox td a').each(function() {
    var coll = $(this).text();
    var new_search = 'search?ln=en&cc='+coll+'&p=&f=&action_search=Search&c='+coll+'&c=&sf=&so=a&rm=&rg=10&sc=1&of=hb';
    $(this).attr('href', new_search);
  });


  /*
   * Links to previous and next records
   */
  $('#bibEditMenu').each(function() {
    var hash = parseUrl(location.href).hash;
    var recid = location.href.split('recid=')[1];
//    alert(location.href + "test 1 - recid: "+recid);
    var prevRecId=recid-1;
    var nextRecId=1+parseInt(recid);
    if (prevRecId<0) prevRecId=0;

//    var prev_href = location.href.replace('recid='+parseInt(recid), 'recid='+prevRecId);
//    var next_href = location.href.replace('recid='+parseInt(recid), 'recid='+nextRecId);
    var prev_href = location.href.split('#')[0]+"#state=edit&recid="+prevRecId;
    var next_href = location.href.split('#')[0]+"#state=edit&recid="+nextRecId;

    if (recid != undefined) {
      $(this).append('<div id="prevNextNav"><a href="'+prev_href+'" class="prev" onClick="return false;">&larr; Prev</a><a href="'+next_href+'" class="next" onClick="return false;">Next &rarr;</a></div>');
    }
/*    $.post(next_href, {"jsondata" : {"recID":recid,"requestType":"getRecord","deleteRecordCache":false,"clonedRecord":false,"ID":12}}, function(data) {
      console.log(data);
    })  */  
  });

  $('#bibEditMenu').on('click', '#prevNextNav a', function() {
    console.log('!!1');
//      alert($('#btnSubmit[disabled]'));
//alert($(this).hasClass('prev'));
//    var sign = ($(this).hasClass('prev')) ? 'minus' : 'plus';
    var canGoOn = false;
      if ($('#btnSubmit').attr('disabled') !== undefined) {
      canGoOn = true;
    } else {
      canGoOn = window.confirm("You have edited the content of the record.\nAre you sure you want to leave without Submit?");
    }
    if (canGoOn) {

      var href = $(this).attr('href');
      window.location = href;
//      alert($(this).attr('class'));
      var recid = href.split('recid=')[1];
      var prevRecId=recid-1;
      var nextRecId=1+parseInt(recid);
      if (prevRecId<0) prevRecId=0;
      var prev_href = href.split('#')[0]+"#state=edit&recid="+prevRecId;
      var next_href = href.split('#')[0]+"#state=edit&recid="+nextRecId;

    $(this).parent().find('a').each(function() {
//      var hash = parseUrl($(this).attr('href')).hash;
//      var recid = hash.match(/^(?:.*recid=)(-?\d)/)[1];
//      alert("test 2 - recid: "+recid + ", " + prevRecId + ", " + nextRecId);
//      var prev_href = location.href.replace('recid='+parseInt(recid), 'recid='+prevRecId);
//      var next_href = location.href.replace('recid='+parseInt(recid), 'recid='+nextRecId);
      if (recid != undefined) {
       if ($(this).attr('class') == 'prev') {
          $(this).attr('href', prev_href);
        } else {
          $(this).attr('href', next_href);
        }
      }
    }
  );

  }



  });
});

function parseUrl( url ) {
    var a = document.createElement('a');
    a.href = url;
    return a;
}

function onclickRecordProceedAfterMerge() { //TP: pridano
  var recid = $('#bibMergeRecInput1').attr('value');
  window.location = '/record/edit/#state=edit&recid='+recid;
}

function onclickPopupImage(href) {
  var image = new Image();
  image.src = href;
  var w=600;
  var h=400;
  newwindow = window.open(href, 'window', 'width='+w+',height='+h+',top=100,left=500,scrollbars=1');
  if (window.focus) {newwindow.focus()}
  if (!newwindow.closed) {newwindow.focus()}
  return false;   
}