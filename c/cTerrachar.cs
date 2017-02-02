using System;
using System.IO;
using System.Reflection;
using Terraria;
using TerrariaApi.Server;
using TShockAPI;
using Newtonsoft.Json;
using System.Drawing;

namespace cTerrachar
{
    public class RelevantInfo
    {
        public string Name { get; set; }

        public int Hair { get; set; }
        public int SkinVariant;

        public Color HairColor;
        public Color SkinColor;
        public Color EyeColor;
        public Color ShirtColor;
        public Color UnderShirtColor;
        public Color PantsColor;
        public Color ShoeColor;

        public int HeadSlot;
        public int BodySlot;
        public int LegsSlot;
        public int HandsOnSlot;
        public int HandsOffSlot;
        public int BackSlot;
        public int FrontSlot;
        public int ShoeSlot;
        public int WaistSlot;
        public int WingSlot;
        public int ShieldSlot;
        public int NeckSlot;
        public int FaceSlot;
        public int BalloonSlot;

    }
	[ApiVersion(2, 0)]
	public class cTerrachar : TerrariaPlugin
	{
		public override string Author => "ChbShoot";
		public override string Description => "Generate player avatars";
        public override string Name => "cTerrachar";
		public override Version Version => Assembly.GetExecutingAssembly().GetName().Version;
        

		public cTerrachar(Main game)
			: base(game)
		{
			Order = 10;
		}

		protected override void Dispose(bool disposing)
		{
			if (disposing)
			{
				ServerApi.Hooks.NetGreetPlayer.Register(this, OnJoin);
			}
		}

		public override void Initialize()
		{
			ServerApi.Hooks.NetGreetPlayer.Register(this, OnJoin);
            ServerApi.Hooks.ServerChat.Register(this, OnChat);
		}

        private void OnChat(ServerChatEventArgs e)
        {
            if (e.Handled || e.Who < 0 || e.Who > Main.player.Length - 1)
                return;

            Player player = Main.player[e.Who];
            // If the player's name is null then it most likely isn't a real player
            if (!String.IsNullOrEmpty(player?.name))
            {
                RelevantInfo relevantPlr = new RelevantInfo();
                relevantPlr.EyeColor = FromXNAToDrawing(player.eyeColor);
                relevantPlr.HairColor = FromXNAToDrawing(player.hairColor);
                relevantPlr.PantsColor = FromXNAToDrawing(player.pantsColor);
                relevantPlr.ShirtColor = FromXNAToDrawing(player.shirtColor);
                relevantPlr.ShoeColor = FromXNAToDrawing(player.shoeColor);
                relevantPlr.SkinColor = FromXNAToDrawing(player.skinColor);
                relevantPlr.UnderShirtColor = FromXNAToDrawing(player.underShirtColor);
                relevantPlr.SkinVariant = player.skinVariant;
                relevantPlr.Hair = player.hair;
                relevantPlr.HeadSlot = player.head;
                relevantPlr.BodySlot = player.body;
                relevantPlr.LegsSlot = player.legs;
                relevantPlr.HandsOnSlot = player.handon;
                relevantPlr.HandsOffSlot = player.handoff;
                relevantPlr.BackSlot = player.back;
                relevantPlr.FrontSlot = player.front;
                relevantPlr.ShoeSlot = player.shoe;
                relevantPlr.WaistSlot = player.waist;
                relevantPlr.WingSlot = player.wings;
                relevantPlr.ShieldSlot = player.shield;
                relevantPlr.NeckSlot = player.neck;
                relevantPlr.FaceSlot = player.face;
                relevantPlr.BalloonSlot = player.balloon;

                relevantPlr.Name = player.name;
                string json = JsonConvert.SerializeObject(relevantPlr);

                File.WriteAllText("{0}.json".SFormat(relevantPlr.Name), json);
            }
        }

        private void OnJoin(GreetPlayerEventArgs e)
		{
			if (e.Handled || e.Who < 0 || e.Who > Main.player.Length - 1)
				return;

			Player player = Main.player[e.Who];
			// If the player's name is null then it most likely isn't a real player
			if (!String.IsNullOrEmpty(player?.name))
			{
                RelevantInfo relevantPlr = new RelevantInfo();
                relevantPlr.EyeColor = FromXNAToDrawing(player.eyeColor);
                relevantPlr.HairColor = FromXNAToDrawing(player.hairColor);
                relevantPlr.PantsColor = FromXNAToDrawing(player.pantsColor);
                relevantPlr.ShirtColor = FromXNAToDrawing(player.shirtColor);
                relevantPlr.ShoeColor = FromXNAToDrawing(player.shoeColor);
                relevantPlr.SkinColor = FromXNAToDrawing(player.skinColor);
                relevantPlr.UnderShirtColor = FromXNAToDrawing(player.underShirtColor);
                relevantPlr.SkinVariant = player.skinVariant;
                relevantPlr.Hair = player.hair;
                relevantPlr.HeadSlot = player.head;
                relevantPlr.BodySlot = player.body;
                relevantPlr.LegsSlot = player.legs;
                relevantPlr.HandsOnSlot = player.handon;
                relevantPlr.HandsOffSlot = player.handoff;
                relevantPlr.BackSlot = player.back;
                relevantPlr.FrontSlot = player.front;
                relevantPlr.ShoeSlot = player.shoe;
                relevantPlr.WaistSlot = player.waist;
                relevantPlr.WingSlot = player.wings;
                relevantPlr.ShieldSlot = player.shield;
                relevantPlr.NeckSlot = player.neck;
                relevantPlr.FaceSlot = player.face;
                relevantPlr.BalloonSlot = player.balloon;

                relevantPlr.Name = player.name;
                string json = JsonConvert.SerializeObject(relevantPlr);

                File.WriteAllText("{0}.json".SFormat(relevantPlr.Name), json);
			}
		}

        public Color FromXNAToDrawing(Microsoft.Xna.Framework.Color clr)
        {
            return Color.FromArgb(clr.A, clr.R, clr.G, clr.B);
        }
	}
}
