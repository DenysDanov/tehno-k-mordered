  /*Last post mobile text trimming*/

  // function trimPostText(){
  //    let windowWidth = $(window).width();
  //    let lastPostText = $('.last-posts ul li:nth-child(n+6)');
  //    if (windowWidth <= 992) lastPostText.remove();
  // }

  function tabsClick(){
    let windowWidth = $(window).width();
    $('.tabs-block').click(function(){
      $('.tabs-block').removeClass('active');
      $(this).addClass('active');
      let tabsNum = $(this).attr('data-tabs');
      $('.tabs-content .tab').removeClass('active');
      $('.tabs-content #tab-' + tabsNum).addClass('active');
      /*Bottom tabs content scroll*/
      if (windowWidth <= 992){
        var target = $('#tab-'+ tabsNum).offset().top-125;
        console.log(target)
        $('body,html').animate({scrollTop:target},500);
      }
    });
  }

  /*set current year in footer*/
  function setCurrentYear(){
    let date = new Date();
    let curYear = date.getFullYear();
    $('.currentDate').text(curYear);
  }

  /*About us mobile text trimming*/
  function trimAboutText(){
     let windowWidth = $(window).width();
     let aboutText = $('.about-us-section .about-text > *');
     let aboutTextLenth = aboutText.text().split('').length;
     if (windowWidth <= 400) aboutText.text(aboutText.text().substring(0, aboutTextLenth / 2).concat('...'))
  }

  function animationHeaderServiceArrow(){
    let animationHeaderServicesArrow = $('.header-services');
    let servicesHeight = $('.header-services-content');
    let arrowHide = $('.down-arrow');
    $(animationHeaderServicesArrow).on("scroll", function() {
      if($(animationHeaderServicesArrow).scrollTop() + $(animationHeaderServicesArrow).height() == $(servicesHeight).height()) arrowHide.css('opacity', '0');
      if($(animationHeaderServicesArrow).scrollTop() + $(animationHeaderServicesArrow).height() !== $(servicesHeight).height()) arrowHide.css('opacity', '1');
    });
  }

  function modalSettings(){
    /*Open mobile menu and close service menu*/
    $('.l-menu-open-btn').click(function () {
      $('.l-menu-mobile').fadeToggle(300);
      $('.mobile-bg').fadeToggle(300);
      $('.l-menu-mobile').css('display', 'flex');
      $('.l-menu-open-btn').toggleClass('active');
      $('.header-services').fadeOut(300);
      $('.class-services-active').fadeOut(300);
    });

    /*Close mobile menu if click in black block*/
    $('.mobile-bg').click(function(e){
      let mobileBg = $(this);
      console.log(mobileBg.is(e.target));
      if (mobileBg.is(e.target) == true) {
        $('.mobile-bg').fadeOut(300);
        $('.l-menu-open-btn').removeClass('active');
        $('.l-menu-mobile').fadeOut(300);
      }
    });

    $('.services').click(function () {
      $('.header-services').fadeIn(300);
       $(this).addClass('active',300)
    });

    $('.header-services > .close').click(function () {
      $('.header-services').fadeOut(300);
      $('.services').removeClass('active');
    });

    /*Close menu and services menu if click no in services menu*/
    $(document).mouseup(function (e){
      let servicesBlock = $(".header-services");
      if (!servicesBlock.is(e.target) && servicesBlock.has(e.target).length === 0)  {
        $('.header-services').fadeOut(300);
        $('.services').removeClass('active');
      }
    });
  }

  function slidersSettings(){
    let windowWidth = $(window).width();

    function topSectionSlider(){
      $('.top-section-slider').slick({
        autoplay: false,
        autoplaySpeed: 2000,
        arrows: true,
        dots: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        swipe: false,
        prevArrow: $('.slider-prev'),
        nextArrow: $('.slider-next')
      });
    }

    function loansContentSlider(){
      if(windowWidth <= 666){
       $('.loans-content').slick({
         arrows: false,
         swipe: true,
         dots: true
       })
      }
    }

    function servicesSolutionsSlider(){
      $('.services-and-solutions-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        dots: true,
        swipe: false,
        responsive: [
          {
            breakpoint: 1156,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              swipe: true
            }
          },
          {
            breakpoint: 667,
            settings: "unslick"
          }
        ]
      });
    }

    function customersSlider(){
      $('.customers-slider').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        vertical: true,
        verticalSwiping: true,
        dots: true,
        arrows: true,
        swipe: false,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              swipe: true
            }
          },
          {
            breakpoint: 523,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              swipe: true,
              arrows:false
            }
          },
        ]
      })
    }

    topSectionSlider();
    loansContentSlider();
    servicesSolutionsSlider();
    customersSlider();
  }


  function popupForm(){
    let count = 0;
    $(".modal-open").fancybox({
      maxWidth  : 1800,
      maxHeight  : 1600,
      fitToView  : false,
      width    : '100%',
      height    : '100%',
      autoSize  : false,
      closeClick  : false,
      openEffect  : 'none',
      closeEffect  : 'none'
    });

    /*Services buttons */

    /*reset form when click buttons*/
    $('.button:not([type="submit"])').click(function(){
      if($('.request-block').parent().hasClass('fancybox-slide') && !$('.input').hasClass('error')){
        $('form')[0].reset();
        $('input').removeClass('error');
        $('.errorText').remove();
      }

      if($(this).attr('data-subcat')){
        let serviceName = $(this).attr('data-subcat');
        $('#requestPopup .input-hidden input[name="service-name"]').val(serviceName);
      }

      if($(this).attr('data-category')){
        let subServiceName = $(this).attr('data-category');
        $('#requestPopup .input-hidden input[name="category-name"]').val(subServiceName);
        let subcat = $(this).closest('div.services-wrapper').find('.services-type a');
        $('#requestPopup .input-hidden input[name="service-name"]').val(subcat.attr('data-subcat'));
        }
      });

      /*close form when we send form success*/
      $('button[type="submit"]').on('click', function(){
        if($('form').valid()){
          $.fancybox.close();
        }
      });
  }


$(document).ready(function() {
  animationBlock($('.loans-content-block'));
  animationBlock($('.about-company-content'));
  animationBlock($('.seo-section'));
  animationBlock($('.we-do-block'));
  modalSettings();
  slidersSettings();
  animationHeaderServiceArrow();
  trimAboutText();
  tabsClick();
  setCurrentYear();
  popupForm();
  validate('.contact-from', {submitFunction:validationCall});
  validate('.top-request-form', {submitFunction:validationCall});
  validate('.contact-form', {submitFunction:validationCall});
  validate('.about-form', {submitFunction:validationCall});
  validate('#requestPopup .popup-form', {submitFunction:validationCall, popNext});
});

$(window).load(function(){

});

$(window).resize(function(){

});
