#/bin/sh
while true; do
	header='Gevent Crawler Demo: '
	menu=("Crawler help" "Edit Crawler config" "Configure crawler in single thread mode (should be done on cron once per 2 or more days)" "Run crawler and view results" "Run crawler and store results" "Exit")
  
	select option in "${menu[@]}"; do
		case $option in
		"Crawler help")
		python ./run_crawler.py -h
		break
		;;
		"Edit Crawler config")
		vi ./config/config.ini
		break
		;;
		"Configure crawler in single thread mode (should be done on cron once per 2 or more days)")
		python ./run_crawler.py -c
		break
		;;
		"Run crawler and view results")
		python ./run_crawler.py -r -v
		break
		;;
		"Run crawler and store results")
		python ./run_crawler.py -r -s
		break
		;;
		"Exit")
		break 2
		;;
		*) echo "Selected option is invalid";;
		esac
	done
done
