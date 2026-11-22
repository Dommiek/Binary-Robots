# LucidXTrader: Open-Source Deriv Trading Bots, Risk Audits and a Bot Builder

LucidXTrader is a free, open-source collection of about 3,350 Deriv Bot (DBot) XML strategies, a searchable shortlist of the bots that pass the risk audit, a few audited "champion" bots, and a read-only toolkit that grades bot risk. Website: [dommiek.github.io/Binary-Robots](https://dommiek.github.io/Binary-Robots/)

[![Open a free Deriv account](https://img.shields.io/badge/Open%20a%20free%20Deriv%20account-demo%20available-red?style=for-the-badge)](https://deriv.com) [![Grade A bots](https://img.shields.io/badge/Grade%20A%20bots-no%20martingale%2C%20stop--loss-2ea44f?style=for-the-badge)](https://dommiek.github.io/Binary-Robots/grade-a.html)

## Quick start

1. [Open a free Deriv account](https://deriv.com). A demo account with virtual funds is available, and an account is needed to run the bots in Deriv Bot.
2. Pick a bot from the [grade A shortlist](https://dommiek.github.io/Binary-Robots/grade-a.html), the [curated champions](champions/README.md), [`Bots_XML/`](Bots_XML/), or the [full index](docs/ROBOTS_INDEX.md).
3. Load the XML file in Deriv Bot or in the [LucidXTrader bot builder](YOUR_LUCIDXTRADER_URL) and run it on a **demo account first**. Study its behavior before risking real money.

> **Risk warning.** Trading involves risk and you can lose your entire stake. Synthetic indices and other derivatives are not suitable for everyone. Nothing here is financial advice or a promise of profit. Test every bot on a demo account first and never trade money you cannot afford to lose. Trading services are provided by Deriv, not by LucidXTrader.

---

## What is in this repository

| Path | Contents |
|---|---|
| [`Bots_XML/`](Bots_XML/) | Community Deriv Bot strategies in Blockly XML, grouped by first letter of the file name |
| [`grade-a.html`](https://dommiek.github.io/Binary-Robots/grade-a.html) | Searchable list of the bots with no stake progression and a session loss limit |
| [`champions/`](champions/) | Three curated bots with strategy guides and audited risk grades |
| [`docs/`](docs/) | [Robot index](docs/ROBOTS_INDEX.md), PDFs and spreadsheets for study |
| [`orstac-agent/`](orstac-agent/) | Open-source, read-only Python toolkit and MCP server: XML auditor, risk math, public Deriv API client. It never trades |

Why use it:
- **Transparent:** every strategy is readable Blockly logic that you can inspect before running it.
- **Risk-aware:** the auditor grades bots from A to D by stake progression (such as martingale) and by the presence of a session stop-loss.
- **Honest numbers:** of the 3,310 bots the auditor can read, only 357 reach grade A. About 2,000 use martingale.

## How to use the bots

1. **Register** a [Deriv account](https://deriv.com) (demo is free).
2. **Explore** the [grade A shortlist](https://dommiek.github.io/Binary-Robots/grade-a.html), the [full index of robots](docs/ROBOTS_INDEX.md) and the [champions](champions/README.md).
3. **Download** the XML file from `Bots_XML/`.
4. **Load** it in Deriv Bot or the [LucidXTrader bot builder](YOUR_LUCIDXTRADER_URL) using the import option.
5. **Test** on a **demo account**. Check the stake after losses and whether the bot stops by itself.
6. **Adjust** parameters such as stake, stop loss and take profit, and measure results over a large sample.

## Audit a bot before you run it

The auditor in [`orstac-agent/`](orstac-agent/) reports a bot's market, contract type, how the stake changes after a loss, whether it has a session loss limit, and a risk grade (A to D). It also computes break-even win rate, position size and the probability of losing streaks. See [`orstac-agent/README.md`](orstac-agent/README.md) for installation and usage.

To rebuild the grade A page after regenerating the audit CSV:

```bash
python orstac-agent/scripts/build_grade_a_page.py
```

## Contributing

Contributions are welcome: fixes, documentation and new bots.

- [Contributing guidelines](CONTRIBUTING.md): how to document a bot (timeframe, market, variables, strategy, best configuration).
- [AI contributing guide](AI_CONTRIBUTING.md): guidance for using AI assistants on this repository.

## Principles

Choose with care. Study the logic, plan your risk management, apply with discipline, measure the results, and repeat. Studying is worth more than any single bot.

## Credits

This repository is based on [ORSTAC](https://github.com/alanvito1/ORSTAC) (Open Source Robots and Technical Analyses Community) by Alan Victor and its contributors, used under the [MIT License](LICENSE). The bots are community contributions and keep their original names and language.

## Links

- [Website](https://dommiek.github.io/Binary-Robots/)
- [Grade A bots](https://dommiek.github.io/Binary-Robots/grade-a.html)
- [LucidXTrader bot builder](YOUR_LUCIDXTRADER_URL)
- [Full robot index](docs/ROBOTS_INDEX.md)
- [Deriv](https://deriv.com)
- [License](LICENSE)

*Risk warning: trading involves risk. Never trade with money you cannot afford to lose. Always use a demo account first. Services are offered by Deriv.*
