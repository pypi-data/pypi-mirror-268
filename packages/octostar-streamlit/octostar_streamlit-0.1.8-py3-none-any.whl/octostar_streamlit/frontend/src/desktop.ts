import { desktopApi } from "@octostar/platform-api";
import {
  AppServiceCallOptions,
  AttachmentType,
  ContextMenuGroup,
  ContextMenuLabels,
  Desktop,
  DesktopActionOptions,
  DesktopStylerContext,
  Entity,
  ExportOptions,
  FileTreeOptions,
  GetAttachmentOptions,
  IDataTransfer,
  ImportZipOptions,
  OsTag,
  Relationship,
  SaveOptions,
  TagAttributes,
  TagInfo,
  Watcher,
  WorkspaceItem,
  WorkspacePermissionValue,
  WorkspaceRecordIdentifier,
  WorkspaceRecordInfo,
  WorkspaceRecordWithRelationships,
} from "@octostar/platform-types";
import {
  MethodCallDef,
  MethodCallHandler,
  None,
  isIdHost,
  isNone,
  noneToUndefined,
} from "./core";

type DesktopApiMethodCall<M extends keyof Desktop, P> = MethodCallDef<
  "desktop",
  M,
  P
>;

type InternalWorkspaceItemIdentifier = { id: string } | WorkspaceItem;

type BridgedDesktop = Omit<
  Desktop,
  | "withProgressBar"
  | "getPasteContext"
  | "showModalTemplate"
  | "getOpenWorkspaceIds"
  | "setOpenWorkspaceIds"
  | "onOpenWorkspaceIdsChanged"
  | "onWorkspaceChanged"
  | "onWorkspaceItemChanged"
  | "onOpenWorkspacesChanged"
>;

const methodCallHandler: MethodCallHandler<BridgedDesktop> = {
  refresh: () => desktopApi().refresh(),

  openWorkspace: (params: InternalWorkspaceItemIdentifier) =>
    desktopApi().openWorkspace(isIdHost(params) ? params.id : params),

  getActiveWorkspace: (params: { prompt: boolean }) =>
    desktopApi().getActiveWorkspace(params.prompt),

  setActiveWorkspace: (params: { id: string }) =>
    desktopApi().setActiveWorkspace(params.id),

  closeWorkspace: (params: InternalWorkspaceItemIdentifier) =>
    desktopApi().closeWorkspace(isIdHost(params) ? params.id : params),

  copy: (params: { source: WorkspaceItem; target: WorkspaceItem }) =>
    desktopApi().copy(params.source, params.target),

  listAllWorkspaces: () => desktopApi().listAllWorkspaces(),

  getOpenWorkspaces: () => desktopApi().getOpenWorkspaces(),

  getAttachment: (params: {
    entity: Entity;
    options: GetAttachmentOptions<AttachmentType> | None;
  }) =>
    desktopApi().getAttachment(params.entity, noneToUndefined(params.options)),

  getStylerOptions: () => desktopApi().getStylerOptions(),

  getStyler: (params: { name: string; context: DesktopStylerContext }) =>
    desktopApi().getStyler(params.name, params.context),

  getWorkspace: (params: InternalWorkspaceItemIdentifier) =>
    desktopApi().getWorkspace(isIdHost(params) ? params.id : params),

  getWorkspaceItems: (params: { os_item_name: string }) =>
    desktopApi().getWorkspaceItems(params.os_item_name),

  applyTag: (params: {
    os_workspace: string;
    tag: OsTag | TagAttributes;
    entity: Entity | Entity[];
  }) => desktopApi().applyTag(params.os_workspace, params.tag, params.entity),

  removeTag: (params: {
    os_workspace: string;
    tag: OsTag | TagAttributes;
    entity: Entity | Entity[];
  }) => desktopApi().removeTag(params.os_workspace, params.tag, params.entity),

  updateTag: (params: { tag: OsTag }) => desktopApi().updateTag(params.tag),

  getItem: (params: InternalWorkspaceItemIdentifier) =>
    desktopApi().getItem(isIdHost(params) ? params.id : params),

  getItems: (params: InternalWorkspaceItemIdentifier[]) =>
    desktopApi().getItems(
      params.map((item) => (isIdHost(item) ? item.id : item))
    ),

  getTags: (params: Entity) => desktopApi().getTags(params),

  getAvailableTags: (params: { entity: Entity; workspace: string | None }) =>
    desktopApi().getAvailableTags(
      params.entity,
      noneToUndefined(params.workspace)
    ),

  getTemplates: () => desktopApi().getTemplates(),

  getTemplate: (params: { name: string; defaultTemplate: string | None }) =>
    desktopApi().getTemplate(
      params.name,
      noneToUndefined(params.defaultTemplate)
    ),

  getSchemaItems: (params: { os_item_content_type: string }) =>
    desktopApi().getSchemaItems(params.os_item_content_type),

  createWorkspace: (params: { name: string }) =>
    desktopApi().createWorkspace(params.name),

  connect: (params: {
    relationship: string | Relationship;
    from_entity: Entity;
    to_entity: Entity;
    os_workspace: string | None;
  }) =>
    desktopApi().connect(
      params.relationship,
      params.from_entity,
      params.to_entity,
      noneToUndefined(params.os_workspace)
    ),

  save: (params: {
    item:
      | WorkspaceItem
      | WorkspaceRecordIdentifier
      | WorkspaceRecordWithRelationships;
    options: SaveOptions | None;
  }) => desktopApi().save(params.item, noneToUndefined(params.options)),

  saveFile: (params: {
    item: WorkspaceItem;
    file: string | File;
    options: SaveOptions | None;
  }) =>
    desktopApi().saveFile(
      params.item,
      params.file,
      noneToUndefined(params.options)
    ),

  import: (params: { items: any[] }) => desktopApi().import(params.items),

  importZip: (params: { file: File; options: ImportZipOptions | None }) =>
    desktopApi().importZip(params.file, noneToUndefined(params.options)),

  export: (params: {
    item: WorkspaceItem | WorkspaceItem[];
    options: ExportOptions | None;
  }) => desktopApi().export(params.item, noneToUndefined(params.options)),

  getFilesTree: (params: {
    workspace_or_folder: WorkspaceItem;
    options: FileTreeOptions | None;
  }) =>
    desktopApi().getFilesTree(
      params.workspace_or_folder,
      noneToUndefined(params.options)
    ),

  open: (params: {
    records: Entity | Entity[];
    options: DesktopActionOptions | None;
  }) => desktopApi().open(params.records, noneToUndefined(params.options)),

  delete: (params: {
    item: WorkspaceRecordIdentifier | WorkspaceRecordIdentifier[];
    recurse: boolean | None;
  }) => desktopApi().delete(params.item, noneToUndefined(params.recurse)),

  searchXperience: (params: {
    taskID: string | None;
    title: string | None;
    defaultConcept: string[] | None;
    disableConceptSelector: boolean | None;
    defaultSearchFields:
      | {
          entity_label: string | None;
          os_textsearchfield: string | None;
        }
      | None;
  }) =>
    desktopApi().searchXperience({
      taskID: noneToUndefined(params.taskID),
      title: noneToUndefined(params.title),
      defaultConcept: noneToUndefined(params.defaultConcept),
      disableConceptSelector: noneToUndefined(params.disableConceptSelector),
      defaultSearchFields: isNone(params.defaultSearchFields)
        ? undefined
        : {
            entity_label: noneToUndefined(
              params.defaultSearchFields.entity_label
            ),
            os_textsearchfield: noneToUndefined(
              params.defaultSearchFields.os_textsearchfield
            ),
          },
    }),

  showTab: (params: {
    app: WorkspaceItem;
    item: WorkspaceItem | None;
    options: DesktopActionOptions | None;
  }) =>
    desktopApi().showTab({
      app: params.app,
      item: noneToUndefined(params.item),
      options: noneToUndefined(params.options),
    }),

  closeTab: (params: {
    app: WorkspaceItem;
    item: WorkspaceItem | None;
    options: DesktopActionOptions | None;
  }) =>
    desktopApi().closeTab({
      app: params.app,
      item: noneToUndefined(params.item),
      options: noneToUndefined(params.options),
    }),

  callAppService: (params: {
    service: string;
    context: object;
    options: AppServiceCallOptions | None;
  }) =>
    desktopApi().callAppService({
      service: params.service,
      context: params.context,
      options: noneToUndefined(params.options),
    }),

  showContextMenu: (
    params:
      | {
          concept: string | None;
          graph:
            | {
                entity: WorkspaceItem;
                relationship_name: string | None;
                relatioship: Relationship | None;
              }
            | None;
          item: WorkspaceItem | None;
          items: WorkspaceItem[] | None;
          workspace:
            | {
                workspace: WorkspaceItem;
                items: WorkspaceItem[];
                workspace_records: Record<string, WorkspaceRecordInfo> | None;
                tags: TagInfo[] | None;
                permission:
                  | { value: WorkspacePermissionValue; label: string }
                  | None;
                isActive: boolean | None;
              }
            | None;
          dataTransfer: IDataTransfer | None;
          eentTopicPrefix: string | None;
          then: (...args: any[]) => any | None;
          x: number;
          y: number;
          openContextMenu: boolean | None;
          onCloseEmit: string | None;
          options:
            | {
                mode: "edit" | "default" | None;
                groups: ContextMenuGroup[] | None;
                labels: ContextMenuLabels | None;
                extras:
                  | any[] /* FIXME: actual type is ItemType but it is not exported */
                  | None;
              }
            | None;
        }
      | { clearContextMenu: true }
  ) => {
    if (params && typeof params === "object" && "clearContextMenu" in params) {
      return desktopApi().showContextMenu({
        clearContextMenu: params.clearContextMenu,
      });
    }

    return desktopApi().showContextMenu({
      concept: noneToUndefined(params.concept),
      graph: noneToUndefined(params.graph),
      item: noneToUndefined(params.item),
      items: noneToUndefined(params.items),
      workspace: isNone(params.workspace)
        ? undefined
        : {
            workspace: params.workspace.workspace,
            items: params.workspace.items,
            workspace_records: noneToUndefined(
              params.workspace.workspace_records
            ),
            tags: noneToUndefined(params.workspace.tags),
            permission: noneToUndefined(params.workspace.permission),
            isActive: noneToUndefined(params.workspace.isActive),
          },
      dataTransfer: noneToUndefined(params.dataTransfer),
      eventTopicPrefix: noneToUndefined(params.eentTopicPrefix),
      then: noneToUndefined(params.then),
      x: params.x,
      y: params.y,
      openContextMenu: noneToUndefined(params.openContextMenu),
      onCloseEmit: noneToUndefined(params.onCloseEmit),
      options: isNone(params.options)
        ? undefined
        : {
            mode: noneToUndefined(params.options.mode),
            groups: noneToUndefined(params.options.groups),
            labels: noneToUndefined(params.options.labels),
            extras: noneToUndefined(params.options.extras),
          },
    });
  },

  showToast: (params: {
    message: string;
    id: string | None;
    description: string | None;
    level: "info" | "success" | "error" | "warning" | None;
    placement:
      | "top"
      | "bottom"
      | "topLeft"
      | "topRight"
      | "bottomLeft"
      | "bottomRight"
      | None;
  }) =>
    desktopApi().showToast({
      message: params.message,
      id: noneToUndefined(params.id),
      description: noneToUndefined(params.description),
      level: noneToUndefined(params.level),
      placement: noneToUndefined(params.placement),
    }),

  clearToast: (params: { id: string }) => desktopApi().clearToast(params.id),

  showProgress: (params: {
    key: string;
    label: string | None;
    job_type: string | None;
    status: "active" | "success" | "exception" | "normal" | None;
  }) =>
    desktopApi().showProgress({
      key: params.key,
      label: noneToUndefined(params.label),
      job_type: noneToUndefined(params.job_type),
      status: noneToUndefined(params.status),
    }),

  showConfirm: (params: {
    title: string;
    icon: string | None;
    content: string | None;
    okText: string | None;
    okButtonProps: { [key: string]: any } | None;
    cancelText: string | None;
    taskID: string | None;
  }) =>
    desktopApi().showConfirm({
      title: params.title,
      icon: noneToUndefined(params.icon),
      content: noneToUndefined(params.content),
      okText: noneToUndefined(params.okText),
      okButtonProps: noneToUndefined(params.okButtonProps),
      cancelText: noneToUndefined(params.cancelText),
      taskID: noneToUndefined(params.taskID),
    }),

  showFileUpload: (params: WorkspaceItem) =>
    desktopApi().showFileUpload(params),

  showCreateEntityForm: (params: {
    os_workspace: string;
    concept: string | None;
  }) =>
    desktopApi().showCreateEntityForm({
      os_workspace: params.os_workspace,
      concept: noneToUndefined(params.concept),
    }),

  addComment: (params: {
    about: Entity;
    comment: {
      os_workspace: string;
      contents: string;
      os_parent_uid: string | None;
      slug: string | None;
    };
  }) =>
    desktopApi().addComment(params.about, {
      os_workspace: params.comment.os_workspace,
      contents: params.comment.contents,
      os_parent_uid: noneToUndefined(params.comment.os_parent_uid),
      slug: noneToUndefined(params.comment.slug),
    }),

  removeComment: (params: { os_workspace: string; comment_id: string }) =>
    desktopApi().removeComment(params.os_workspace, params.comment_id),

  addWatchIntent: (params: { entity: Entity; watcher: Watcher }) =>
    desktopApi().addWatchIntent(params.entity, params.watcher),

  removeWatchIntent: (params: { os_workspace: string; intent_id: string }) =>
    desktopApi().removeWatchIntent(params.os_workspace, params.intent_id),

  getWorkspacePermission: (params: { os_workspace: string[] }) =>
    desktopApi().getWorkspacePermission(params.os_workspace),

  getUser: () => desktopApi().getUser(),

  deployApp: (params: { app: WorkspaceItem }) =>
    desktopApi().deployApp(params.app),

  undeployApp: (params: { app: WorkspaceItem }) =>
    desktopApi().undeployApp(params.app),

  whoami: () => desktopApi().whoami(),
};

export const forwardDesktopApiMethodCallToPlatform = (
  methodCall: DesktopApiMethodCall<keyof BridgedDesktop, unknown>
) => {
  const handler = methodCallHandler[methodCall.method];
  if (!handler) {
    throw new Error(`Unknown method: ${methodCall.method}`);
  }

  return handler(methodCall.params);
};
