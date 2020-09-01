/*
Theme Name: Prixto Agency HTML Template.
Author: WebZoneThemes
Author URL: http://www.webzonethemes.com/
Version: 1.0.0
*/
(function ($)
{
	'use strict';
	/*===============================================*/
	/*  Bckground image on html tag
 /*===============================================*/
	$("[data-background]").each(function ()
	{
		$(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
	});
	/*===============================================*/
	/*  Navigation
 /*===============================================*/
	$('.navbar-toggle').on('click', function (event)
	{
		$(this).toggleClass('open');
		$('#navigation').slideToggle(400);
	});
	$('.navigation-menu>li').slice(-1).addClass('last-elements');
	$('.menu-arrow,.submenu-arrow').on('click', function (e)
	{
		if ($(window).width() < 992)
		{
			e.preventDefault();
			$(this).parent('li').toggleClass('open').find('.submenu:first').toggleClass('open');
		}
	});
	$(".navigation-menu a").each(function ()
	{
		if (this.href == window.location.href)
		{
			$(this).parent().addClass("active");
			$(this).parent().parent().parent().addClass("active");
			$(this).parent().parent().parent().parent().parent().addClass("active");
		}
	});
	// Clickable Menu
	$(".has-submenu a").click(function ()
	{
		if (window.innerWidth < 992)
		{
			if ($(this).parent().hasClass('open'))
			{
				$(this).siblings('.submenu').removeClass('open');
				$(this).parent().removeClass('open');
			}
			else
			{
				$(this).siblings('.submenu').addClass('open');
				$(this).parent().addClass('open');
			}
		}
	});
	$('.mouse-down').on('click', function (event)
	{
		var $anchor = $(this);
		$('html, body').stop().animate({
			scrollTop: $($anchor.attr('href')).offset().top - 72
		}, 1500, 'easeInOutExpo');
		event.preventDefault();
	});
	//Sticky
	$(window).scroll(function ()
	{
		var scroll = $(window).scrollTop();
		if (scroll >= 50)
		{
			$(".sticky").addClass("nav-sticky");
		}
		else
		{
			$(".sticky").removeClass("nav-sticky");
		}
	});
	/*===============================================*/
	/*  Slick Slider
 /*===============================================*/
	//Slick Slider (Banner Slider)
	$(".px-modern-Slider").slick({
		autoplay: true,
		autoplaySpeed: 10000,
		speed: 600,
		slidesToShow: 1,
		slidesToScroll: 1,
		pauseOnHover: false,
		dots: true,
		pauseOnDotsHover: true,
		cssEase: 'linear',
		// fade:true,
		draggable: false,
		prevArrow: '<button class="PrevArrow"></button>',
		nextArrow: '<button class="NextArrow"></button>',
		responsive: [{
			breakpoint: 991,
			settings: {
				arrows: true,
			}
		}, {
			breakpoint: 768,
			settings: {
				arrows: true,
			}
		}, {
			breakpoint: 600,
			settings: {
				arrows: false,
			}
		}, {
			breakpoint: 480,
			settings: {
				arrows: false,
			}
		}]
	});
	// Slick Slider (Portfolio Section)
	$('.px-work-slider').slick({
		centerMode: true,
		centerPadding: '60px',
		slidesToShow: 3,
		arrows: true,
		prevArrow: $('.px-prev-arrow'),
		nextArrow: $('.px-next-arrow'),
		responsive: [{
			breakpoint: 991,
			settings: {
				arrows: false,
				centerMode: false,
				slidesToShow: 2
			}
		}, {
			breakpoint: 768,
			settings: {
				arrows: false,
				centerMode: false,
				slidesToShow: 2
			}
		}, {
			breakpoint: 600,
			settings: {
				arrows: false,
				centerMode: false,
				slidesToShow: 1
			}
		}, {
			breakpoint: 480,
			settings: {
				arrows: false,
				centerMode: false,
				slidesToShow: 1
			}
		}]
	});
	// Slick Slider (Testimonials Section)
	$('.px-clients-slider').slick({
		centerMode: false,
		centerPadding: '60px',
		slidesToShow: 3,
		draggable: true,
		autoplay: true,
		autoplaySpeed: 3000,
		dots: true,
		arrows: false,
		infinite: true,
		responsive: [{
			breakpoint: 991,
			settings: {
				arrows: false,
				centerMode: false,
				centerPadding: '40px',
				slidesToShow: 2
			}
		}, {
			breakpoint: 768,
			settings: {
				arrows: false,
				centerMode: false,
				centerPadding: '40px',
				slidesToShow: 1
			}
		}, {
			breakpoint: 480,
			settings: {
				arrows: false,
				centerMode: false,
				centerPadding: '40px',
				slidesToShow: 1
			}
		}]
	});
	// Slick Slider (partner Section)
	$('.px-partner-slider').slick({
		slidesToShow: 4,
		arrows: false,
		draggable: true,
		autoplay: true,
		autoplaySpeed: 3000,
		responsive: [{
			breakpoint: 991,
			settings: {
				arrows: false,
				slidesToShow: 3
			}
		}, {
			breakpoint: 768,
			settings: {
				arrows: false,
				slidesToShow: 2
			}
		}, {
			breakpoint: 480,
			settings: {
				arrows: false,
				slidesToShow: 1
			}
		}]
	});
	/*===============================================*/
	/*  Video Popup
 /*===============================================*/
	$('#play-video').on('click', function (e)
	{
		e.preventDefault();
		$('#video-overlay').addClass('open');
		$("#video-overlay").append('<iframe width="560" height="315" src="https://www.youtube.com/embed/ngElkyQ6Rhs" frameborder="0" allowfullscreen></iframe>');
	});
	$('.video-overlay, .video-overlay-close').on('click', function (e)
	{
		e.preventDefault();
		close_video();
	});
	$(document).keyup(function (e)
	{
		if (e.keyCode === 27)
		{
			close_video();
		}
	});
	function close_video()
	{
		$('.video-overlay.open').removeClass('open').find('iframe').remove();
	}
	/*===============================================*/
	/*  Counter JS
 /*===============================================*/
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});
	/*===============================================*/
	/*  Accordian JS
 /*===============================================*/
	$("#accordion").on("hide.bs.collapse show.bs.collapse", e =>
	{
		$(e.target).prev().find("i:last-child").toggleClass("fa-minus fa-plus");
	});
	/*===============================================*/
	/*  filter gallery
 /*===============================================*/
	$(document).ready(function ()
	{
		$('.gallery-grid').isotope(function ()
		{
			'.filter-box'
		});
		$('.filter-gallery>li').click(function ()
		{
			$('.filter-gallery>li').removeClass('active');
			$(this).addClass('active');
			var selector = $(this).attr('data-filter');
			$('.gallery-grid').isotope({
				filter: selector
			})
			return false;
		});
	});
	/*===============================================*/
	/*  PRE LOADING
 /*===============================================*/
	$(window).on('load', function ()
	{
		$('.loader').delay(500).fadeOut('slow');
	});
})(jQuery);