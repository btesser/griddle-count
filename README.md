# Griddle Count

A small, self-hosted traffic dashboard built for Burger of the Day. Apache sends one timestamp for each successful board request to a Python process. The process increments a daily UTC counter in SQLite. A second script renders the most recent 30 days with traffic as a private HTML report.

Counts include bots and reloads. Offline opens and navigation within the page produce no request. The counter stores only dates and totals. Apache's other access logs follow your server configuration.

## Install on Debian or Ubuntu

Use Apache 2.4, Python 3, cron and htpasswd (apache2-utils). Enable the Apache alias, headers, proxy and authentication modules. The example assumes an existing HTTPS virtual host and the www-data group. Run these commands as root from the checkout.

```sh
install -d -m 0755 /var/lib/botd-stats /var/www/botd-report
install -m 0755 count.py report.py /var/lib/botd-stats/
htpasswd -cB /etc/apache2/botd-report.passwd owner
chown root:www-data /etc/apache2/botd-report.passwd
chmod 0640 /etc/apache2/botd-report.passwd
/var/lib/botd-stats/report.py
echo '* * * * * root /var/lib/botd-stats/report.py' > /etc/cron.d/botd-report
```

Use the htpasswd creation command for a new password file only. Install the contents of `apache.conf.example` inside your HTTPS virtual host, before any catch-all proxy rule. Keep the scripts and their directory writable only by the administrator because Apache can launch piped loggers as root. Check the configuration with `apachectl configtest`, then reload Apache. Visit the homepage and open `/analytics/` with the owner login after the next cron tick.

To adapt the dashboard to another site, edit the title in report.py and the request path filter in the Apache example.

## License

MIT.
