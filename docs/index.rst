Welcome to Steamship-LangChain
=================================

⚡ Deploy 🦜️🔗LangChain apps to production with 🚢 Steamship ⚡

Getting Started
----------------

Checkout the below guide for a walkthrough of how to move your application to production.

- `Getting Started Documentation <./getting_started/getting_started.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :name: getting_started
   :hidden:

   getting_started/getting_started.md


Adapters
-----------

We've built adapters for LangChain's most important modules and components.
Using these adapters enables you to leverage Steamship's infrastructure including its scalable execution framework, caching, and databases.

To guide you through the upgrade process we've included how-to guides and some examples for each LangChain module.

Have a look at our `Coverage Page <./getting_started/getting_started.html>`_ for an overview of what is currently supported.


- `Prompts <./adapters/prompts.html>`_

- `LLMs <./adapters/llms.html>`_

- `Callbacks <./adapters/callbacks.html>`_

- `Document Loaders <./adapters/document_loaders.html>`_

- `Chains <./adapters/chains.html>`_

- `VectorStores <./adapters/vectorstores.html>`_

- `Agents <./adapters/agents.html>`_

- `Memory <./adapters/memory.html>`_


.. toctree::
   :maxdepth: 1
   :caption: Adapters
   :name: adapters
   :hidden:

   ./adapters/prompts.md
   ./adapters/llms.rst
   ./adapters/callbacks.rst
   ./adapters/document_loaders.rst
   ./adapters/chains.md
   ./adapters/agents.md
   ./adapters/memory.md
   ./adapters/vectorstores.rst

Use Cases
----------

Here are some of the common use cases supported by Steamship:

- `ChatGPT <./use_cases/chatgpt.html>`_
- `QuestionAnswering <./use_cases/question_answering.html>`_


.. toctree::
   :maxdepth: 1
   :caption: Use Cases
   :name: use_cases
   :hidden:

   ./use_cases/chatgpt.ipynb
   ./use_cases/question_answering.md


Coverage and Roadmap
----------------------

Support for LangChain is currently in alpha. But we're all in on creating the best LangChain infra stack.

We've compiled a status page to track what modules & use-cases are officially supported by Steamship.

Something's missing? We'd love to hear from you. Please reach out to: hello@steamship.com, or join us on our Discord.


- `Our Coverage <./getting_started/getting_started.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Coverage
   :name: coverage
   :hidden:

   support/coverage.md