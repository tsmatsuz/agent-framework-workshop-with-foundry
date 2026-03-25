# Agent Framework (with Microsoft Foundry) workshop (Python)

The purpose of this repository is to provide step-by-step learning to use fundamental Agent Framework functionalities with Microsoft Foundry (Foundry v2).<br>
More advanced topics - such as, multi-agent design patterns, custom objects, etc - are out of scope in this repository.

1. [Getting started](./01_get_started.ipynb)
2. [Trace Agent](./02_trace.ipynb)
3. [Thread (Conversation)](./03_session.ipynb)
4. [Hosted Tools](./04_hosted_tools.ipynb)
5. [Foundry Tools](./05_foundry_tools.ipynb)
6. [Memory and personalization (Context Provider/Memory Provider)](./06_memory.ipynb)
7. [Agent Skills](./07_skills.ipynb)
8. [Workflows](./08_workflow.ipynb)
9. [Human-in-the-loop (HITL)](./09_human_in_the_loop.ipynb)
10. [Hosted Agents in Microsoft Foundry](./10_hosted_agents.ipynb)

## Prerequisites

Prepare (create) Microsoft Azure subscription.

Create a new Microsoft Foundry resource in [Azure Portal](https://portal.azure.com/).<br>
You will find that this operation creates 2 resources in Microsoft Azure - Foundry resource (parent resource) and Foundry project resource.

Next, go to Microsoft Foundry Portal for Foundry project you have just created.<br>
In this workshop, we need new Foundry v2 project, not v1 project. So toggle on "New Foundry" to go to new Foundry Portal.<br>
In Foundry Portal (new portal), deploy Azure OpenAI model which is supported in Azure OpenAI Responses API. (See [here](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses?view=foundry&tabs=python-key#model-support) for the supported models.)

Install the required Python modules as follows.

```
# required in all exercises
pip install agent-framework --pre
# required in lesson 2
pip install azure-monitor-opentelemetry
```

> Note : All source code in this repository is experimented by using Agent Framework version ```1.0.0rc5```. If it doesn't work in the latest version, please install the specific version as follows. (The version will be frequently updated, because it's now in preview.)  
> ```pip install agent-framework-azure-ai==1.0.0rc5 agent-framework==1.0.0rc5 agent-framework-core==1.0.0rc5```

Throughtout this workshop, we'll use Azure CLI credential.  
For this reason, install Azure CLI (```az``` command), and login to Azure by running ```az login``` command.

> Note : You cannot use API key in new ```azure-ai-projects```. (See [here](https://learn.microsoft.com/en-us/answers/questions/5587848/how-to-use-api-key-in-azure-ai-foundry).) Use Entra ID users (or service principal) in production.

Clone this repository in your working environment.

```
git clone https://github.com/tsmatsuz/agent-framework-workshop-with-foundry
cd agent-framework-workshop-with-foundry
```

Copy ```.env.example``` as ```.env```, open ```.env``` in editor, and set variables according to your environment.  
The variable ```AZURE_AI_PROJECT_ENDPOINT``` has the format - "```https://[FOUNDRY-RESOURCE-NAME].services.ai.azure.com/api/projects/[PROJECT-NAME]```" (This can be retrieved from home in Microsoft Foundry dashboard.)

Run notebooks.

```
jupyter notebook
```

In each exercise, we also need another preparations and settings, but these additional settings are written in each exercise.  
(Especially, in Lesson 10, we also need ```azd``` CLI command and another Foundry project. See [Lesson10](./10_hosted_agents.ipynb) for details.)

> Note : By installing ```agent-framework```, the required sub-packages in Agent Framework are all installed. See [here](https://github.com/microsoft/agent-framework/tree/main/python/packages) for the list of sub-packages.

## Validating Your Configuration

Before running the notebooks, you can validate your configuration:

```python
from utils import validate_config
validate_config()
```

Or from the command line:

```bash
python -m utils.validate_config
```

## Common Setup Mistakes

| ❌ Wrong | ✅ Correct |
|----------|-----------|
| `https://xxx.openai.azure.com/...` | `https://xxx.services.ai.azure.com/api/projects/...` |
| Azure OpenAI resource endpoint | Foundry **project** endpoint |

**How to find the correct endpoint:**
1. Go to [Azure Portal](https://portal.azure.com/) → your **Foundry project** resource (not the parent Foundry resource)
2. Or open the **Microsoft Foundry Portal** dashboard for your project
3. The endpoint is displayed on the overview/home page

**Other common issues:**
- Not logged into Azure CLI → Run `az login`
- Model not deployed → Deploy a Responses API compatible model (gpt-4o, gpt-4.1, etc.) in your Foundry project
- Wrong subscription → Ensure `az account show` displays the correct subscription

## Official samples

The purpose of this repository is to provide step-by-step learning with clear explanation (background) to use fundamental Agent Framework functionalities with Microsoft Foundry (Foundry v2).

In [official GitHub samples](https://github.com/microsoft/agent-framework/tree/main/python/samples/getting_started/agents/azure_ai), you can find more advanced code samples to provide a wide variety of scenarios. (Several examples in this repository are based on this official repository.)

*Tsuyoshi Matsuzaki @ Microsoft Asia*
