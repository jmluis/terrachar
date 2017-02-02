using System;
using System.Reflection;
using Terraria;
using TerrariaApi.Server;
using TShockAPI;
using Newtonsoft.Json;
using Rests;
using System.Collections.Generic;

namespace cTerrachar
{
    public class RelevantInfo
    {
        public string Name { get; set; }

        public int Hair { get; set; }
        public int SkinVariant;

        public int[] HairColor;
        public int[] SkinColor;
        public int[] EyeColor;
        public int[] ShirtColor;
        public int[] UnderShirtColor;
        public int[] PantsColor;
        public int[] ShoeColor;

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? HeadSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? BodySlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? LegsSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? HandsOnSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? HandsOffSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? BackSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? FrontSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? ShoeSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? WaistSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? WingSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? ShieldSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? NeckSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? FaceSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? BalloonSlot;

        public static RelevantInfo GetRelevance(Player player)
        {
            RelevantInfo relevantPlr = new RelevantInfo();
            relevantPlr.EyeColor = new int[] { player.eyeColor.R, player.eyeColor.G, player.eyeColor.B };
            relevantPlr.HairColor = new int[] { player.hairColor.R, player.hairColor.G, player.hairColor.B };
            relevantPlr.PantsColor = new int[] { player.pantsColor.R, player.pantsColor.G, player.pantsColor.B };
            relevantPlr.ShirtColor = new int[] { player.shirtColor.R, player.shirtColor.G, player.shirtColor.B };
            relevantPlr.ShoeColor = new int[] { player.shoeColor.R, player.shoeColor.G, player.shoeColor.B };
            relevantPlr.SkinColor = new int[] { player.skinColor.R, player.skinColor.G, player.skinColor.B };
            relevantPlr.UnderShirtColor = new int[] { player.underShirtColor.R, player.underShirtColor.G, player.underShirtColor.B };
            relevantPlr.SkinVariant = player.skinVariant;
            relevantPlr.Hair = player.hair;
            relevantPlr.HeadSlot = (player.head < 1) ? (int?)null : player.head;
            relevantPlr.BodySlot = player.body < 1 ? (int?)null : player.body;
            relevantPlr.LegsSlot = player.legs < 1 ? (int?)null : player.legs;
            relevantPlr.HandsOnSlot = player.handon < 1 ? (int?)null : player.handon;
            relevantPlr.HandsOffSlot = player.handoff < 1 ? (int?)null : player.handoff;
            relevantPlr.BackSlot = player.back < 1 ? (int?)null : player.head;
            relevantPlr.FrontSlot = player.front < 1 ? (int?)null : player.front;
            relevantPlr.ShoeSlot = player.shoe < 1 ? (int?)null : player.shoe;
            relevantPlr.WaistSlot = player.waist < 1 ? (int?)null : player.waist;
            relevantPlr.WingSlot = player.wings < 1 ? (int?)null : player.wings;
            relevantPlr.ShieldSlot = player.shield < 1 ? (int?)null : player.shield;
            relevantPlr.NeckSlot = player.neck < 1 ? (int?)null : player.neck;
            relevantPlr.FaceSlot = player.face < 1 ? (int?)null : player.face;
            relevantPlr.BalloonSlot = player.balloon < 1 ? (int?)null : player.balloon;
            relevantPlr.Name = player.name;
            return relevantPlr;
        }

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

        public override void Initialize()
        {
            TShock.RestApi.Register(new RestCommand("/cterrachar/active_players", getPlayers));
            TShock.RestApi.Register(new RestCommand("/cterrachar/player", getPlayer));
        }

        private object getPlayer(RestRequestArgs args)
        {
            string strName = args.Parameters["name"];
            if (string.IsNullOrEmpty(strName))
            {
                return new RestObject()
                {
                    { "error" , "expected player name in 'name'" }
                };
            }

            List<TSPlayer> plrs = TShock.Utils.FindPlayer(strName);
            if (plrs.Count != 1)
            {
                return new RestObject()
                {
                    { "error", string.Format("{0} players with name '{1}'", plrs.Count, strName) }
                };
            }
            return new RestObject()
            {
                { "player", RelevantInfo.GetRelevance(plrs[0].TPlayer) }
            };
        }

        private object getPlayers(RestRequestArgs args)
        {
            List<RelevantInfo> relevantPlayers = new List<RelevantInfo>();
            for (int i = 0; i < Main.player.Length; i++)
            {
                Player player = Main.player[i];
                if (!String.IsNullOrEmpty(player?.name))
                {
                    relevantPlayers.Add(RelevantInfo.GetRelevance(player));
                }
            }
            return new RestObject()
            {
                {"count", relevantPlayers.Count },
                {"players", relevantPlayers }
            };
        }


    }
}
