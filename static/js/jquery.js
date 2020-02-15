/*
 * imgMask
 * 基于jQuery的扩展，实现一个容器下多个子元素透明度蒙板效果
 * 调用方式：obj.imgMask(options);
 * 参数说明：opacity，鼠标移动上之后的蒙板透明度，范围是0-1，默认“0.3”
 *           html_element，子元素的html容器，默认是“div”
 * 开发者：吕歆
 * 版本：0.1
 * 最后更新时间 2012年3月22日 14:21:57
 */
(function($){
    var ver = 0.1;
    /*
     * make_mask
     * 生成蒙板外框
     * obj，要增加蒙板的对象
     * settings,配置
     */
    function make_mask(obj,settings){
        obj.children().each(function(){
            var o = $(this);
            var a = o.children();
            var mask = $("<div></div>");
            mask.css({
                width:function(){
                    return o.css("width");
                },
                height:function(){
                    return o.css("height");
                },
                top:"0px",
                left:"0px",
                background:'#000',
                opacity:'0',
                position:'absolute',
                display:'block',
                overflow:'hidden',
                filter:'alpha(opacity=0)',
                cursor:'pointer'
            });

            mask.appendTo(o);
            bind(mask,settings);
        });
        
        obj.bind("mouseout",function(){
            $(this).children().find("div").css("opacity","0");
        });
    }
    /*
     * bind
     * 绑定蒙板事件
     * mask,蒙板对象
     * settings，设置
     */
    function bind(mask,settings){
        mask.bind("mouseover",function(){
            $(mask.parents(settings.html_element)[0]).siblings().find("div").css("opacity",settings.opacity);
            mask.css("opacity","0");
        });
    };

    $.fn.imgMask = function(options){
        if(this.children().length<2)
            return this;
        var settings = {
            opacity:'0.3',
            html_element:'a'
        };
        if(options){
            $.extend(settings,options);
        }
        make_mask(this,settings);
        return this;
    };
    $.fn.imgMask.ver = function(){
        return ver;
    };
})(jQuery);
