const GITHUB_API = 'https://api.github.com';

/**
 * GitHub REST 프록시. Vercel 환경변수 GH_TOKEN(또는 GITHUB_TOKEN)으로 인증합니다.
 * query: path — api.github.com 뒤에 붙는 전체 문자열 (예: repos/o/r/pulls?state=all)
 */
module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.statusCode = 405;
    res.setHeader('Allow', 'GET');
    res.end();
    return;
  }

  const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN;
  if (!token) {
    res.statusCode = 503;
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify({ message: 'GH_TOKEN or GITHUB_TOKEN is not set' }));
    return;
  }

  const repo = process.env.GITHUB_REPO || 'seoyeonDev/doit-algorithm-study';
  const allowedPrefix = `repos/${repo}/`;

  const raw = req.query.path;
  if (typeof raw !== 'string' || !raw.startsWith('repos/')) {
    res.statusCode = 400;
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify({ message: 'Invalid path' }));
    return;
  }

  if (raw.includes('..') || raw.includes('\n') || raw.includes('\r')) {
    res.statusCode = 400;
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify({ message: 'Invalid path' }));
    return;
  }

  if (!raw.startsWith(allowedPrefix)) {
    res.statusCode = 403;
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify({ message: 'Forbidden' }));
    return;
  }

  const url = `${GITHUB_API}/${raw}`;

  try {
    const ghRes = await fetch(url, {
      headers: {
        Accept: 'application/vnd.github+json',
        Authorization: `Bearer ${token}`,
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'doit-algorithm-study-vercel-proxy',
      },
    });

    const ct = ghRes.headers.get('content-type');
    if (ct) res.setHeader('Content-Type', ct);

    const body = Buffer.from(await ghRes.arrayBuffer());
    res.statusCode = ghRes.status;
    res.end(body);
  } catch {
    res.statusCode = 502;
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify({ message: 'GitHub request failed' }));
  }
};
