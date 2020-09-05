from django.contrib import admin

from control_panel.models import (
	site_title,
	slideshow,
	video,
	services,
	work_samples,
	our_team,
	our_customers,
	site_theme,
	)
admin.site.register(site_title)
admin.site.register(slideshow)
admin.site.register(video)
admin.site.register(services)
admin.site.register(work_samples)
admin.site.register(our_team)
admin.site.register(our_customers)
admin.site.register(site_theme)
