# New Hire Bootstrapper

New Hire Bootstrapper is a Korean-first, on-premises workflow for preparing,
onboarding, and supporting new employees through Slack or the dashboard.

> **Modified version notice (2026-10-20):** New Hire Bootstrapper adds a
> Korean-first interface, deployment-owned onboarding defaults, and a
> reproducible on-premises deployment. It is based on
> [chiefonboarding/ChiefOnboarding](https://github.com/chiefonboarding/ChiefOnboarding)
> and remains licensed as a whole under GNU AGPL-3.0. The corresponding source
> for this deployed version is available from
> [dalsoop/new-hire-bootstrapper](https://github.com/dalsoop/new-hire-bootstrapper).

![chiefonboarding timeline overview](docs/static/timeline-overview.png)

## Features
- **Automatically provision user accounts and trigger webhooks**, see [https://integrations.chiefonboarding.com](https://integrations.chiefonboarding.com) for a list of integrations or create your own!
- **Pre-boarding**: onboarding doesn't start on day 1, it starts before that. Build pre-boarding pages to welcome new hires before they start.
- **To do items**: keep track of the things that your new hires need to do and allow them to fill in forms.
- **Resources**: let them search through the knowledge base and complete courses so they are quickly up to speed with colleagues.
- **Sequences**: drip feeding items over time or based on the completion of a to do item. Avoid the overwhelming feeling.  
- **Badges**: reward new hires for the things they have done. This also helps to keep them motivated.
- **Introductions**: introduce people to new hires.
- **Admin to do items**: collaborate with colleagues on things that need to be done for the new hire.
- **Multilingual**: Korean, English, Dutch, Portuguese, German, Turkish, French, Spanish, and Japanese are supported.
- **Timezones**: It doesn't matter where your new hire lives. You can adjust the timezone per new hire, so they don't get messages in the middle of the night!
- **Slack bot and dashboard**: your new hires can use the dashboard or the Slack bot. Both provide all features and can be used standalone.
- **Customizable**: use your logo, add your color scheme, change the email template and customize the bot to your liking.
- **Transparency, freedom, and privacy**: New Hire Bootstrapper is completely open-source and licensed under AGPLv3.
- Host it yourself on your own infrastructure.

## On-premises deployment

Use [`docker-compose.production.yml`](docker-compose.production.yml) with a
deployment-owned `runtime.env`, `database.env`, external PostgreSQL volume, and
external `new-hire-bootstrapper` network.

## Upstream project

New Hire Bootstrapper preserves the upstream architecture and compatibility of
ChiefOnboarding 2.5.0. Refer to the
[upstream documentation](https://docs.chiefonboarding.com) for the underlying
application model and integration details.

## Support

This software is provided as-is under its open-source license. Use this
repository's issue tracker for questions and reproducible bug reports.

## Security issues

Do not disclose potential vulnerabilities in a public issue. Use the
repository's private security reporting channel.

## License
This project is licensed under the AGPLv3 License - see the [LICENSE.md](LICENSE.md) file for details.
