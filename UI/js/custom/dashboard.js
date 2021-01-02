$(function () {
    //Json data by api call for order table
    $.get(orderListApiUrl, function (response) {
        if(response) {
            var table = '';
            var totalCost = 0;
            $.each(response, function(index, order) {
                totalCost += parseFloat(order.total);
                table += '<tr>' +
                    '<td>'+ order.datetime +'</td>'+
                    '<td>'+ order.order_id +'</td>'+
                    '<td>'+ order.customer_name +'</td>'+
                    '<td>'+ order.total.toFixed(2) +' Pounds</td>'+
                    '<td>'+ '<button type="button" class="btn btn-xs btn-warning pull-center" data-toggle="modal" data-target="#productModal'+order.order_id+'">'+
                    'show details</button></td>'+
                    '</tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' Pounds</b></td></tr>';

            $("table").find('tbody').empty().html(table);
        }
    });
});