COUNTRIES = (
		("Nigeria", "Nigeria"),
		("Ghana", "Ghana"),
		("Kenya", "Kenya"),
	)


TITLE = (
			('Mr', 'Mr'),
			('Mrs','Mrs'),
			('Dr', 'Dr'),
	)

PUB_STATUS  =  (
	  		('New',  'New'),
	  		('sent_to_external_editor', 'sent_to_external_editor'),
	  		('Processing',  'Processing'),
	  		('Published',   'Published'),
	  		('Rejected',    'Rejected'),
   )

MEDIA_PLATFORM = (
			("Newspaper", "Newspaper"),
			("Blog","Blog"),
	)

BOUQUET  =  (
			("Single", "Single"),
			("Basic", "Basic"),
			("Maxi", "Maxi"),
			("Super Maxi", "Super Maxi"),
	)

PACKAGES  =  (
			("basic", "Basic"),
			("regular", "Regular"),
			("premium", "Premium"),
			("premium-plus", "Premium Plus"),
	)


PURCHASE_STATUS  =  (
			("New", "New"),
			("Processing","Processing"),
			("Pending","Pending"),
			("Rejected","Rejected"),
			("Closed", "Closed"),

	)



PAYMENT_OPTIONS  =  (
			("Bank Deposit", "Bank Deposit"),
			("Card Payment", "Card Payment"),
			("Bank Transfer", "Bank Transfer"),
	)



PAYMENT_STATUS = (
			("verified", "verified"),
			("pending","pending"),
			("failed","failed"),
	)



BANKS     =   (
			("Diamond Bank", "Diamond Bank"),
			("GTB","GTB")

	)


ECONOMY_SECTOR = (
		("Finance", "Finance"),
	)


FEEDBACK_STATUS = (
		("Open","Open"),
		("Closed","Closed"),
		("Pending","Pending"),
	)

BUSINESS_TYPE = (   ('NA', 'NA',),
					('Company', 'Company',),
                	('Individual', 'Individual',),
        )

COMPANY_TYPE  = (   ('NA', 'NA',),
					('Public', 'Public',),
                	('Private', 'Private',),
        )

PR_FREQUENCY  = (
					('NA', 'NA',),
					('weekly',  'Weekly',),
					('monthly', 'Monthly',),
					('several-times-a-month', 'Several Times a Month',),
					('quartely', 'Quartely',),
	                ('annually', 'Annually',),
	                ('first-time-user', 'First Time User',),
                
        )

ACTION_STATUS = (
				 ('new', 'new'),
				 ('contacted', 'contacted',),
				 ('in_progress','In progress',),
                 ('closed', 'closed',),  
        	)

REQUEST_OUTCOME   =  (
				   ('pending', 'pending'),
				   ('success', 'success',),
				   ('declined','declined',),
				   ('deferred','deferred',),
				   ('dropped','dropped',)
				)


SERVICE_TYPE = (
		('Press Release Distribution', 'Press Release Distribution'),
		('Content Writing and Marketing', 'Content Marketing'),
		('Advertising', 'Advertising'),
		('SME Marketing', 'SME Marketing'),
		('Sales and Marketing', 'Sales and Marketing'),
		('Events Bureau','Events Bureau'),
		('Blogger Distribution', 'Blogger Distribution'),
	)


ACTION_TYPE = (
		('select_service',  'select service'),
		('submit_content',  'submit content'),
		('request_service', 'request service'),
	)

BOOLEAN_CHOICES = (('yes','yes'),
					('no','no'),
					)

BLOG_CATEGORIES   =   (
				('Top_blogs', 'Top_blogs'),
				('Technology','technology'),
				)


