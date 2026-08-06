from odoo import models
from odoo.exceptions import AccessError


class MailMessage(models.Model):
    _inherit = "mail.message"

    def _check_message_lock_permission(self):
        if not self.env.user.has_group("base.group_system"):
            raise AccessError(
                "این عملیات فقط برای کاربران Administrator مجاز است."
            )

    def write(self, vals):
        self._check_message_lock_permission()
        return super().write(vals)

    def unlink(self):
        self._check_message_lock_permission()
        return super().unlink()
