"""
Type annotations for bedrock-agent service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_agent.client import AgentsforBedrockClient

    session = Session()
    client: AgentsforBedrockClient = session.client("bedrock-agent")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ActionGroupStateType, KnowledgeBaseStateType
from .paginator import (
    ListAgentActionGroupsPaginator,
    ListAgentAliasesPaginator,
    ListAgentKnowledgeBasesPaginator,
    ListAgentsPaginator,
    ListAgentVersionsPaginator,
    ListDataSourcesPaginator,
    ListIngestionJobsPaginator,
    ListKnowledgeBasesPaginator,
)
from .type_defs import (
    ActionGroupExecutorTypeDef,
    AgentAliasRoutingConfigurationListItemTypeDef,
    APISchemaTypeDef,
    AssociateAgentKnowledgeBaseResponseTypeDef,
    CreateAgentActionGroupResponseTypeDef,
    CreateAgentAliasResponseTypeDef,
    CreateAgentResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DeleteAgentAliasResponseTypeDef,
    DeleteAgentResponseTypeDef,
    DeleteAgentVersionResponseTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteKnowledgeBaseResponseTypeDef,
    GetAgentActionGroupResponseTypeDef,
    GetAgentAliasResponseTypeDef,
    GetAgentKnowledgeBaseResponseTypeDef,
    GetAgentResponseTypeDef,
    GetAgentVersionResponseTypeDef,
    GetDataSourceResponseTypeDef,
    GetIngestionJobResponseTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    IngestionJobFilterTypeDef,
    IngestionJobSortByTypeDef,
    KnowledgeBaseConfigurationTypeDef,
    ListAgentActionGroupsResponseTypeDef,
    ListAgentAliasesResponseTypeDef,
    ListAgentKnowledgeBasesResponseTypeDef,
    ListAgentsResponseTypeDef,
    ListAgentVersionsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListIngestionJobsResponseTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PrepareAgentResponseTypeDef,
    PromptOverrideConfigurationTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    StartIngestionJobResponseTypeDef,
    StorageConfigurationTypeDef,
    UpdateAgentActionGroupResponseTypeDef,
    UpdateAgentAliasResponseTypeDef,
    UpdateAgentKnowledgeBaseResponseTypeDef,
    UpdateAgentResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateKnowledgeBaseResponseTypeDef,
    VectorIngestionConfigurationTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AgentsforBedrockClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AgentsforBedrockClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AgentsforBedrockClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#exceptions)
        """

    def associate_agent_knowledge_base(
        self,
        *,
        agentId: str,
        agentVersion: str,
        description: str,
        knowledgeBaseId: str,
        knowledgeBaseState: KnowledgeBaseStateType = ...,
    ) -> AssociateAgentKnowledgeBaseResponseTypeDef:
        """
        Associates a knowledge base with an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.associate_agent_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#associate_agent_knowledge_base)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#close)
        """

    def create_agent(
        self,
        *,
        agentName: str,
        agentResourceRoleArn: str = ...,
        clientToken: str = ...,
        customerEncryptionKeyArn: str = ...,
        description: str = ...,
        foundationModel: str = ...,
        idleSessionTTLInSeconds: int = ...,
        instruction: str = ...,
        promptOverrideConfiguration: PromptOverrideConfigurationTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateAgentResponseTypeDef:
        """
        Creates an agent that orchestrates interactions between foundation models, data
        sources, software applications, user conversations, and APIs to carry out tasks
        to help
        customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.create_agent)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#create_agent)
        """

    def create_agent_action_group(
        self,
        *,
        actionGroupName: str,
        agentId: str,
        agentVersion: str,
        actionGroupExecutor: ActionGroupExecutorTypeDef = ...,
        actionGroupState: ActionGroupStateType = ...,
        apiSchema: APISchemaTypeDef = ...,
        clientToken: str = ...,
        description: str = ...,
        parentActionGroupSignature: Literal["AMAZON.UserInput"] = ...,
    ) -> CreateAgentActionGroupResponseTypeDef:
        """
        Creates an action group for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.create_agent_action_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#create_agent_action_group)
        """

    def create_agent_alias(
        self,
        *,
        agentAliasName: str,
        agentId: str,
        clientToken: str = ...,
        description: str = ...,
        routingConfiguration: Sequence[AgentAliasRoutingConfigurationListItemTypeDef] = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateAgentAliasResponseTypeDef:
        """
        Creates an alias of an agent that can be used to deploy the agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.create_agent_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#create_agent_alias)
        """

    def create_data_source(
        self,
        *,
        dataSourceConfiguration: DataSourceConfigurationTypeDef,
        knowledgeBaseId: str,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        serverSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef = ...,
        vectorIngestionConfiguration: VectorIngestionConfigurationTypeDef = ...,
    ) -> CreateDataSourceResponseTypeDef:
        """
        Sets up a data source to be added to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.create_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#create_data_source)
        """

    def create_knowledge_base(
        self,
        *,
        knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef,
        name: str,
        roleArn: str,
        storageConfiguration: StorageConfigurationTypeDef,
        clientToken: str = ...,
        description: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base that contains data sources from which information can
        be queried and used by
        LLMs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.create_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#create_knowledge_base)
        """

    def delete_agent(
        self, *, agentId: str, skipResourceInUseCheck: bool = ...
    ) -> DeleteAgentResponseTypeDef:
        """
        Deletes an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.delete_agent)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#delete_agent)
        """

    def delete_agent_action_group(
        self,
        *,
        actionGroupId: str,
        agentId: str,
        agentVersion: str,
        skipResourceInUseCheck: bool = ...,
    ) -> Dict[str, Any]:
        """
        Deletes an action group in an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.delete_agent_action_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#delete_agent_action_group)
        """

    def delete_agent_alias(
        self, *, agentAliasId: str, agentId: str
    ) -> DeleteAgentAliasResponseTypeDef:
        """
        Deletes an alias of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.delete_agent_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#delete_agent_alias)
        """

    def delete_agent_version(
        self, *, agentId: str, agentVersion: str, skipResourceInUseCheck: bool = ...
    ) -> DeleteAgentVersionResponseTypeDef:
        """
        Deletes a version of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.delete_agent_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#delete_agent_version)
        """

    def delete_data_source(
        self, *, dataSourceId: str, knowledgeBaseId: str
    ) -> DeleteDataSourceResponseTypeDef:
        """
        Deletes a data source from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.delete_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#delete_data_source)
        """

    def delete_knowledge_base(self, *, knowledgeBaseId: str) -> DeleteKnowledgeBaseResponseTypeDef:
        """
        Deletes a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.delete_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#delete_knowledge_base)
        """

    def disassociate_agent_knowledge_base(
        self, *, agentId: str, agentVersion: str, knowledgeBaseId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a knowledge base from an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.disassociate_agent_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#disassociate_agent_knowledge_base)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#generate_presigned_url)
        """

    def get_agent(self, *, agentId: str) -> GetAgentResponseTypeDef:
        """
        Gets information about an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_agent)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_agent)
        """

    def get_agent_action_group(
        self, *, actionGroupId: str, agentId: str, agentVersion: str
    ) -> GetAgentActionGroupResponseTypeDef:
        """
        Gets information about an action group for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_agent_action_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_agent_action_group)
        """

    def get_agent_alias(self, *, agentAliasId: str, agentId: str) -> GetAgentAliasResponseTypeDef:
        """
        Gets information about an alias of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_agent_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_agent_alias)
        """

    def get_agent_knowledge_base(
        self, *, agentId: str, agentVersion: str, knowledgeBaseId: str
    ) -> GetAgentKnowledgeBaseResponseTypeDef:
        """
        Gets information about a knowledge base associated with an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_agent_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_agent_knowledge_base)
        """

    def get_agent_version(
        self, *, agentId: str, agentVersion: str
    ) -> GetAgentVersionResponseTypeDef:
        """
        Gets details about a version of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_agent_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_agent_version)
        """

    def get_data_source(
        self, *, dataSourceId: str, knowledgeBaseId: str
    ) -> GetDataSourceResponseTypeDef:
        """
        Gets information about a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_data_source)
        """

    def get_ingestion_job(
        self, *, dataSourceId: str, ingestionJobId: str, knowledgeBaseId: str
    ) -> GetIngestionJobResponseTypeDef:
        """
        Gets information about a ingestion job, in which a data source is added to a
        knowledge
        base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_ingestion_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_ingestion_job)
        """

    def get_knowledge_base(self, *, knowledgeBaseId: str) -> GetKnowledgeBaseResponseTypeDef:
        """
        Gets information about a knoweldge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_knowledge_base)
        """

    def list_agent_action_groups(
        self, *, agentId: str, agentVersion: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAgentActionGroupsResponseTypeDef:
        """
        Lists the action groups for an agent and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_agent_action_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_agent_action_groups)
        """

    def list_agent_aliases(
        self, *, agentId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAgentAliasesResponseTypeDef:
        """
        Lists the aliases of an agent and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_agent_aliases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_agent_aliases)
        """

    def list_agent_knowledge_bases(
        self, *, agentId: str, agentVersion: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAgentKnowledgeBasesResponseTypeDef:
        """
        Lists knowledge bases associated with an agent and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_agent_knowledge_bases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_agent_knowledge_bases)
        """

    def list_agent_versions(
        self, *, agentId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAgentVersionsResponseTypeDef:
        """
        Lists the versions of an agent and information about each version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_agent_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_agent_versions)
        """

    def list_agents(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListAgentsResponseTypeDef:
        """
        Lists the agents belonging to an account and information about each agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_agents)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_agents)
        """

    def list_data_sources(
        self, *, knowledgeBaseId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data sources in a knowledge base and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_data_sources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_data_sources)
        """

    def list_ingestion_jobs(
        self,
        *,
        dataSourceId: str,
        knowledgeBaseId: str,
        filters: Sequence[IngestionJobFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: IngestionJobSortByTypeDef = ...,
    ) -> ListIngestionJobsResponseTypeDef:
        """
        Lists the ingestion jobs for a data source and information about each of them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_ingestion_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_ingestion_jobs)
        """

    def list_knowledge_bases(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases in an account and information about each of them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_knowledge_bases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_knowledge_bases)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List all the tags for the resource you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#list_tags_for_resource)
        """

    def prepare_agent(self, *, agentId: str) -> PrepareAgentResponseTypeDef:
        """
        Creates a `DRAFT` version of the agent that can be used for internal testing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.prepare_agent)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#prepare_agent)
        """

    def start_ingestion_job(
        self,
        *,
        dataSourceId: str,
        knowledgeBaseId: str,
        clientToken: str = ...,
        description: str = ...,
    ) -> StartIngestionJobResponseTypeDef:
        """
        Begins an ingestion job, in which a data source is added to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.start_ingestion_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#start_ingestion_job)
        """

    def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Associate tags with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#untag_resource)
        """

    def update_agent(
        self,
        *,
        agentId: str,
        agentName: str,
        agentResourceRoleArn: str,
        foundationModel: str,
        customerEncryptionKeyArn: str = ...,
        description: str = ...,
        idleSessionTTLInSeconds: int = ...,
        instruction: str = ...,
        promptOverrideConfiguration: PromptOverrideConfigurationTypeDef = ...,
    ) -> UpdateAgentResponseTypeDef:
        """
        Updates the configuration of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.update_agent)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#update_agent)
        """

    def update_agent_action_group(
        self,
        *,
        actionGroupId: str,
        actionGroupName: str,
        agentId: str,
        agentVersion: str,
        actionGroupExecutor: ActionGroupExecutorTypeDef = ...,
        actionGroupState: ActionGroupStateType = ...,
        apiSchema: APISchemaTypeDef = ...,
        description: str = ...,
        parentActionGroupSignature: Literal["AMAZON.UserInput"] = ...,
    ) -> UpdateAgentActionGroupResponseTypeDef:
        """
        Updates the configuration for an action group for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.update_agent_action_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#update_agent_action_group)
        """

    def update_agent_alias(
        self,
        *,
        agentAliasId: str,
        agentAliasName: str,
        agentId: str,
        description: str = ...,
        routingConfiguration: Sequence[AgentAliasRoutingConfigurationListItemTypeDef] = ...,
    ) -> UpdateAgentAliasResponseTypeDef:
        """
        Updates configurations for an alias of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.update_agent_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#update_agent_alias)
        """

    def update_agent_knowledge_base(
        self,
        *,
        agentId: str,
        agentVersion: str,
        knowledgeBaseId: str,
        description: str = ...,
        knowledgeBaseState: KnowledgeBaseStateType = ...,
    ) -> UpdateAgentKnowledgeBaseResponseTypeDef:
        """
        Updates the configuration for a knowledge base that has been associated with an
        agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.update_agent_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#update_agent_knowledge_base)
        """

    def update_data_source(
        self,
        *,
        dataSourceConfiguration: DataSourceConfigurationTypeDef,
        dataSourceId: str,
        knowledgeBaseId: str,
        name: str,
        description: str = ...,
        serverSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef = ...,
        vectorIngestionConfiguration: VectorIngestionConfigurationTypeDef = ...,
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates configurations for a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.update_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#update_data_source)
        """

    def update_knowledge_base(
        self,
        *,
        knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef,
        knowledgeBaseId: str,
        name: str,
        roleArn: str,
        storageConfiguration: StorageConfigurationTypeDef,
        description: str = ...,
    ) -> UpdateKnowledgeBaseResponseTypeDef:
        """
        Updates the configuration of a knowledge base with the fields that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.update_knowledge_base)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#update_knowledge_base)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_agent_action_groups"]
    ) -> ListAgentActionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_agent_aliases"]
    ) -> ListAgentAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_agent_knowledge_bases"]
    ) -> ListAgentKnowledgeBasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_agent_versions"]
    ) -> ListAgentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_agents"]) -> ListAgentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ingestion_jobs"]
    ) -> ListIngestionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/client/#get_paginator)
        """
