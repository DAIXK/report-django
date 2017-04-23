/**
 * Created by daixk on 17-3-6.
 */
var class_list = ['bad','alls','bads','hardwares','softwares','nas'];
function get_table_head() {
                        var a =[];
                        for(var x=1; x<=$('#head th:gt(0)').length; x++){
                            a.push($('#head th:eq('+x+')').text());
                        };
                        return a;
                    };
function get_table_pcs() {
                        var a =[];
                        for(var x=1; x<=$('#pcs td:gt(0)').length; x++){
                            a.push(+$('#pcs td:eq('+x+')').text());
                        };
                        return a;
                    };
function make_list(object) {
    var list = [];
    for (x in object){
        list += x+',';
    };
    list=list.slice(0,list.length-1);
    list=list.split(',');
    return list;
};
function make_two_data(object,data1,data2,key) {
                        var list={};
                        for (x in object[data1]){
                           list[x] = object[data1][x]+object[data2][x];
                        };
                        return object[key]=list;
                    };
function make_three_data(object,data1,data2,data3,key) {
                        var list={};
                        for (x in object[data1]){
                            list[x] = object[data1][x]+object[data2][x]+object[data3][x];
                        };
                        return object[key]=list;

                    };
function table_head(object,class_list,sale_list,list) {
                     var result = [];
                     var back_list = [];
                     var bad_list = [];
                     var all_list = [];
                     for (var x=0; x<class_list.length; x++){
                        var str ='';
                        for (var y=0; y<list.length; y++){
                            switch (class_list[x]){
                                case 'bad':
                                    str += '<td>' + (object[list[y]]['hardware'] + object[list[y]]['software']) + '</td>';
                                    break;
                                case 'alls':
                                    str += '<td>' + (object[list[y]]['all'] / sale_list[y] * 100).toFixed(2) + '%' + '</td>';
                                    back_list.push(+(object[list[y]]['all'] / sale_list[y] * 100).toFixed(2));
                                    all_list.push(+object[list[y]]['all']);
                                    break;
                                case 'bads':
                                    str += '<td>' + ((object[list[y]]['hardware'] + object[list[y]]['software']) / sale_list[y] * 100).toFixed(2) + '%' + '</td>';
                                    bad_list.push(+((object[list[y]]['hardware'] + object[list[y]]['software']) / sale_list[y] * 100).toFixed(2))
                                    break;
                                case 'hardwares':
                                    str += '<td>' + ((object[list[y]]['hardware']) / sale_list[y] * 100).toFixed(2) + '%' + '</td>';
                                    break;
                                case 'softwares':
                                    str += '<td>' + ((object[list[y]]['software']) / sale_list[y] * 100).toFixed(2) + '%' + '</td>';
                                    break;
                                case 'nas':
                                    str += '<td>' + ((object[list[y]]['na']) / sale_list[y] * 100).toFixed(2) + '%' + '</td>';
                                    break;
                            };
                        };
                        $('.'+class_list[x]+'').after(str);
                     };
                     result.push(back_list,bad_list,all_list);
                     return result;
                 };
function table_body(object,list) {
                     for (x in object[list[0]]){
                         var str='';
                         for (var y=0;y<list.length;y++){
                            str += '<td>'+object[list[y]][x]+'</td>'
                         };
                         $('.'+x+'').after(str);
                    };
                 };
function hightchars(x_list,back_list,bad_list,all_list,name,max) {
                    $('#container').highcharts({
                        exporting: {
                                enabled: false
                             },
                        credits:{
                            text:'',
                        },
                        chart: {
                            zoomType: 'xy'
                        },
                        title: {
                            text: name
                        },
                        subtitle: {
                            text: ''
                        },
                        xAxis: {
                            categories:x_list
                        },
                        yAxis: [{ // Primary yAxis

                            labels: {
                                format: '{value}%',
                                style: {
                                    color: Highcharts.getOptions().colors[1]
                                }
                            },
                            title: {
                                text: 'Percentage',
                                style: {
                                    color: Highcharts.getOptions().colors[1]
                                }
                            }
                        }, { // Secondary yAxis
                            title: {
                                text: 'Sales',
                                style: {
                                    color: Highcharts.getOptions().colors[0]
                                }
                            },
                            labels: {
                                format: '{value}pcs',
                                style: {
                                    color: Highcharts.getOptions().colors[0]

                                }
                            },
                            //双精度，控制另外的Y轴值
                            opposite: true,
                            min:0,
                            max:max,
                        }],
                        legend: {
                            layout: 'vertical',
                            align: 'right',
                            verticalAlign: 'middle',
                            borderWidth: 0
                        },
                        plotOptions: {
                            spline: {
                                dataLabels: {
                                    enabled: true,
                                    format:'{y} %'
                                },
                                enableMouseTracking: true
                            },
                            column:{
                              dataLabels:{
                                  enabled:true
                              }
                            }
                        },
                        series: [{
                            name: '总返回数',
                            type: 'column',
                            yAxis: 1,
                            //柱形大小
                            maxPointWidth: 50,
                            data:all_list,
                            tooltip: {
                                valueSuffix: 'pcs'
                            }
                        }, {
                            name: '返回率',
                            type: 'spline',
                            data:back_list ,
                            tooltip: {
                                valueSuffix: '%'
                            }
                        },
                            {
                            name: '实际不良率',
                            type: 'spline',
                            data: bad_list,
                            tooltip: {
                                valueSuffix: '%'
                            },


                        }]
                    });
                };