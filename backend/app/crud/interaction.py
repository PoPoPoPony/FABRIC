from app.db.models import Interaction as DB_Interaction
from app.schemas.interaction import Interaction



def create_interaction(
        interaction: Interaction,
        db
    ):
    DB_interaction = db.query(DB_Interaction).filter(DB_Interaction.user_id==interaction.user_id, DB_Interaction.baby_id==interaction.baby_id, DB_Interaction.user_role==interaction.user_role).first()

    if not DB_interaction:
        new_interaction = DB_Interaction(
            user_id=interaction.user_id,
            baby_id=interaction.baby_id,
            user_role=interaction.user_role
        )

        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)


def check_interaction(baby_id, user_id, user_role, db):
    interaction = db.query(DB_Interaction).filter(DB_Interaction.user_id == user_id, DB_Interaction.baby_id == baby_id, DB_Interaction.user_role == user_role).first()
    # 若user沒有與baby bind的話
    if interaction:
        return True
    else:
        return False