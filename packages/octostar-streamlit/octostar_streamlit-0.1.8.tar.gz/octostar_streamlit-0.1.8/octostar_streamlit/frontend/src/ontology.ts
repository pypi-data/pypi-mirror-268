import {
  Concept,
  Entity,
  Inheritance,
  Ontology,
  QueryResponse,
  Relationship,
  RelationshipCountResult,
  Unsubscribe,
  WorkspaceRelationship,
} from "@octostar/platform-types";
import {
  MethodCallDef,
  MethodCallHandler,
  None,
  isNone,
  noneToUndefined,
} from "./core";
import { ontologyApi } from "@octostar/platform-api";

type OntologyMethodCall<M, P> = MethodCallDef<"ontology", M, P>;

type OntologyBridge = Omit<Ontology, "sendQueryT">;

const methodCallHandler: MethodCallHandler<OntologyBridge> = {
  cancelQueries: function (params: { context: string }): Promise<void> {
    return ontologyApi().cancelQueries(params.context);
  },
  getAvailableOntologies: function (): Promise<string[]> {
    return ontologyApi().getAvailableOntologies();
  },
  getWorkspaceRelationshipRecords: function (params: {
    entity: Entity;
    relationship: Relationship;
  }): Promise<WorkspaceRelationship[]> {
    return ontologyApi().getWorkspaceRelationshipRecords(
      params.entity,
      params.relationship
    );
  },
  clearRelationshipCache: function (params: {
    entity: Entity;
    relationship: Relationship | string;
  }): Promise<void> {
    return ontologyApi().clearRelationshipCache(
      params.entity,
      params.relationship
    );
  },
  getConnectedEntities: function (params: {
    entity: Entity;
    relationship: Relationship | string;
    force_refresh: boolean | None;
  }): Promise<Entity[]> {
    return ontologyApi().getConnectedEntities(
      params.entity,
      params.relationship,
      noneToUndefined(params.force_refresh)
    );
  },
  getConceptByName: function (params: {
    concept_name: string;
  }): Promise<Concept | undefined> {
    return ontologyApi().getConceptByName(params.concept_name);
  },
  getConcepts: function (): Promise<Map<string, Concept>> {
    return ontologyApi().getConcepts();
  },
  getEntity: function (params: {
    entity: Entity;
    refresh: boolean | None;
    skip_side_effects: boolean | None;
  }): Promise<Entity> {
    return ontologyApi().getEntity(
      params.entity,
      noneToUndefined(params.refresh),
      noneToUndefined(params.skip_side_effects)
    );
  },
  getOntologyName: function (): Promise<string> {
    return ontologyApi().getOntologyName();
  },
  getRelationshipCount: function (params: {
    entity: Entity;
    relationship: Relationship | string;
    force_refresh: boolean | None;
  }): Promise<RelationshipCountResult> {
    return ontologyApi().getRelationshipCount(
      params.entity,
      params.relationship,
      noneToUndefined(params.force_refresh)
    );
  },
  getConceptForEntity: function (params: {
    entity: Entity;
  }): Promise<Concept | undefined> {
    return ontologyApi().getConceptForEntity(params.entity);
  },
  getRelationshipsForEntity: function (params: {
    entity: Entity;
  }): Promise<Relationship[]> {
    return ontologyApi().getRelationshipsForEntity(params.entity);
  },
  sendQuery: function (params: {
    query: string;
    options:
      | {
          context: string | None;
          low_priority: boolean | None;
        }
      | None;
  }): Promise<QueryResponse> {
    return ontologyApi().sendQuery(
      params.query,
      isNone(params.options)
        ? undefined
        : {
            context: noneToUndefined(params.options.context),
            lowPriority: noneToUndefined(params.options.low_priority),
          }
    );
  },
  getSysInheritance: function (): Promise<Inheritance[]> {
    return ontologyApi().getSysInheritance();
  },
  subscribe: function (): Promise<Unsubscribe> {
    throw new Error("Function not implemented.");
  },
  consistentUUID: function (params: {
    name: string;
    namespace: string | None;
  }): Promise<string> {
    return ontologyApi().consistentUUID(
      params.name,
      noneToUndefined(params.namespace)
    );
  },
};

export const forwardOntologyApiMethodCallToPlatform = (
  call: OntologyMethodCall<keyof OntologyBridge, unknown>
) => {
  const methodHandler = methodCallHandler[call.method];
  if (!methodHandler) {
    throw new Error(`Method ${call.method} not found`);
  }

  return methodHandler(call.params);
};
