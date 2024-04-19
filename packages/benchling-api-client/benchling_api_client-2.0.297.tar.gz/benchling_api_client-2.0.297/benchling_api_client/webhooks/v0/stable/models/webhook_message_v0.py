from typing import Union

from ..extensions import UnknownType
from ..models.app_activate_requested_webhook_v2 import AppActivateRequestedWebhookV2
from ..models.app_deactivated_webhook_v2 import AppDeactivatedWebhookV2
from ..models.canvas_initialize_webhook_v0 import CanvasInitializeWebhookV0
from ..models.canvas_initialize_webhook_v2 import CanvasInitializeWebhookV2
from ..models.canvas_interaction_webhook_v0 import CanvasInteractionWebhookV0
from ..models.canvas_interaction_webhook_v2 import CanvasInteractionWebhookV2
from ..models.lifecycle_activate_webhook_v0 import LifecycleActivateWebhookV0
from ..models.lifecycle_deactivate_webhook_v0 import LifecycleDeactivateWebhookV0

WebhookMessageV0 = Union[
    CanvasInteractionWebhookV0,
    CanvasInitializeWebhookV0,
    LifecycleActivateWebhookV0,
    LifecycleDeactivateWebhookV0,
    CanvasInteractionWebhookV2,
    CanvasInitializeWebhookV2,
    AppActivateRequestedWebhookV2,
    AppDeactivatedWebhookV2,
    UnknownType,
]
