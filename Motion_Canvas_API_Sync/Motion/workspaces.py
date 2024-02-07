import requests
import Motion_Canvas_API_Sync.Motion.secrets as secrets

api_key = secrets.api_key
secret_workspace_name = secrets.workspace_name


class Workspace:
    def __init__(
        self,
        *,
        id: str = None,
        name: str = secret_workspace_name,
        api_key: str = api_key,
    ):
        self.api_key = api_key
        self.url = "https://api.usemotion.com/v1/workspaces"
        self.headers = {"Accept": "application/json", "X-API-Key": api_key}

        if id:
            self.workspace = self.__from_id(id)
        elif name:
            self.workspace = self.__from_name(name)
        else:
            raise Exception("ID and Name can not both be null")

    def __from_name(self, name: str) -> dict:
        motion_workspaces = requests.get(url=self.url, headers=self.headers).json()
        for workspace in motion_workspaces["workspaces"]:
            if workspace["name"] == name:
                return workspace
        raise Exception("Workspace Name does not exist")

    def __from_id(self, id: str) -> dict:
        motion_workspaces = requests.get(url=self.url, headers=self.headers).json()
        for workspace in motion_workspaces["workspaces"]:
            if workspace["id"] == id:
                return workspace
        raise Exception("Workspace id does not exist")

    def get_id(self):
        return self.workspace["id"]

    # This method is fucking stupid. Technically don't need it, but calling Workspace().workspace looks wack af, and doesn't make sense.
    # Could not make __init__ return a dict, which is probably a good decision anyway.

    # In hindsight, I should probably delete this class and make these methods part of the module.

    # Nope, beceause then how would you change the API key? Stupid it is, it's 12:46 and I should probably go to bed, but this is fun because this is new and usefull.

    # Its 12:49 and I just realized I could just pass the api key to each method... There's only two, I'm a fucking idiot but I'm too tired to fix things rn.
    # Realistically it works perfectly fine right now, it's just not as pretty as it could be. I should spend my time writing new modules, but here I am writing comments.
    def get_workspace(self):
        return self.workspace


if __name__ == "__main__":
    print(Workspace())
