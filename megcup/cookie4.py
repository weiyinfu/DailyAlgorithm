import math
import functools
import argparse
import random
import json
try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest

# Your token here
CONTEST_TOKEN = 'ca8ae4c6213879776d79b134a0798e4e3d6ad1cfd00deefc4001b45a6f5a32db'
PRACTICE_TOKEN = 'bd23a5f6a54b1004cfeed00dfc1da6d3e4e8970a431b97d6779783126c4ea8ac'

def get_token(token_type):
	if token_type == 'contest':
		return CONTEST_TOKEN
	elif token_type=='practice':
		return PRACTICE_TOKEN
	else:
		return None


def get_api_root(token_type):
	if token_type == 'contest':
		return 'http://47.93.114.77:13555/sequence'
	elif token_type=='practice':
		return 'http://47.90.105.15:13555/sequence'
	else:
		return None


def _check_resp(resp):
	if resp['status'] == 'succeed':
		return True, resp['data']
	return False, resp


def check_resp_deco(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		ret = func(*args, **kwargs)
		succ, rst = _check_resp(ret)
		if not succ:
			raise RuntimeError(rst)
		return rst

	return wrapper


class Sequence:
	"""
	API wrapper for a single problem sequence
	"""
	def __init__(self, token, seq_id, api_root):
		self.token = token
		self.seq_id = seq_id
		self.api_root = api_root
		if self.token==None:
			rnd=random.Random(seq_id*1357)
			order=list(range(10000))
			rnd.shuffle(order)
			self.nexts=[0 for i in range(10000)]
			for i in range(len(order)):
				if i!=len(order)-1:
					self.nexts[order[i]]=order[i+1]
				else:
					self.nexts[order[i]]=-1
			self.head=order[0]
			numbers=sorted([rnd.randrange(2**31-10001) for i in range(10000)])
			for i in range(len(numbers)):
				numbers[i]+=i
			self.numbers=[0 for i in range(10000)]
			for i in range(len(numbers)):
				self.numbers[order[i]]=numbers[i]
			if rnd.choice([True,False]):
				self._target=rnd.choice(self.numbers)
				self.ground_truth=True
			else:
				self._target=rnd.randrange(2**31-10001)
				self.ground_truth=self._target in self.numbers
			self.query_count=0
			self.passed=False
			self._finished=False

	@property
	def base_url(self):
		return self.api_root + '/{token}/seq/{seq_id}'.format(
				token=self.token, seq_id=self.seq_id)

	def _get(self, suffix):
		url = self.base_url + suffix
		print('url: {}'.format(url))
		rst = json.loads(urlrequest.urlopen(url).read().decode('utf8'))
		print('response: {}'.format(rst))
		return rst

	@check_resp_deco
	def get_status(self):
		if self.token is None:
			return {
				'status':'succeed',
				'data':{
					'count':self.query_count,
					'finished':self._finished,
					'length':10000,
					'passed':('unfinished' if not self._finished else self.passed),
					'target':self._target,
					'head_index':self.head,
				}
			}
		return self._get('/status')

	@property
	def length(self):
		return self.get_status()['length']

	@property
	def target(self):
		"""target value to look up
		"""
		return self.get_status()['target']

	@property
	def head_index(self):
		"""head index of the linked list in the array
		"""
		return self.get_status()['head_index']

	@property
	def finished(self):
		return self.get_status()['finished']

	@property
	def history(self):
		return self.get_status()['history']

	@property
	def count(self):
		return self.get_status()['count']

	@check_resp_deco
	def query(self, index):
		if self.token==None:
			if self._finished:
				return {
					'status':'error',
					'data':{
						'message':"sequence already finished",
						'valid':False,
					}
				}
			elif self.query_count>=400:
				self._finished=True
				return {
					'status':'succeed',
					'data':{
						'message':"number of queries exceeds limit (400), you've failed the test case",
						'valid':False,
					}
				}
			elif index<0 or index>=10000:
				return {
					'status':'error',
					'data':{
						'message':"invalid index",
						'valid':False,
					}
				}
			else:
				self.query_count+=1
				return {
					'status':'succeed',
					'data':{
						'index':index,
						'next':self.nexts[index],
						'valid':True,
						'value':self.numbers[index]
					}
				}
		else:
			return self._get('/query/{}'.format(index))

	@check_resp_deco
	def report(self, result):
		"""
		:param result: 'exist' or 'not_exist'
		"""
		if self.token==None:
			if self._finished:
				return {
					'status':'error',
					'data':{
						'message':"sequence already finished"
					}
				}
			elif result not in ['exist','not_exist']:
				return {
					'status':'error',
					'data':{
						'index':'result must be either "exist" or "not_exist"'
					}
				}
			self._finished=True
			self.passed=(result=='exist')==self.ground_truth
			return {
				'status':'succeed',
				'data':{
					'passed':self.passed
				}
			}
		return self._get('/report/{}'.format(result))


def verbose_get(url):
	print('url: {}'.format(url))
	rst = json.loads(urlrequest.urlopen(url).read().decode('utf8'))
	print('response: {}'.format(rst))
	return rst

def get_overall_status(api_root, token):
	res = verbose_get(api_root + '/' + token + '/status')
	if res['status'] != 'succeed':
		raise RuntimeError(res)
	return res['data']


def get_pass_token(api_root, token):
	return get_overall_status(api_root, token)['pass_token']


def reset_token(api_root, token):
	res = verbose_get(api_root + '/' + token + '/reset')
	if res['status'] != 'succeed':
		raise RuntimeError(res)
	return res['data']


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--token-type', default='local',
			choices=['contest', 'practice','local'])
	parser.add_argument( '--noreset', action='store_true',
			help='do not reset a practice token')
	args = parser.parse_args()

	token = get_token(args.token_type)
	api_root = get_api_root(args.token_type)

	if token==PRACTICE_TOKEN and not args.noreset:
		reset_token(api_root, token)

	seqs=[]
	for seq_id in range(20):
		seq = Sequence(token, seq_id, api_root)
		seqs.append(seq)
		n = seq.length
		cur_idx = seq.head_index
		target = seq.target
                Max = -1
                pos = 0

                for i in xrange(0,190):
                    r = seq.query(i)
                    if (r['value'] <= target and r['value'] > Max):
                        Max = r['value']
                        pos = i
                cur_idx = pos
                finish = 0
                for i in xrange(0,190):
                    if (cur_idx != -1):
                        r = seq.query(cur_idx)
                        if (r['value'] == target):
                            seq.report('exist')
                            finish = 1
                            break
                        cur_idx = r['next']

                if (not finish):
                    seq.report('not_exist')




                '''
		while cur_idx != -1:
			r = seq.query(cur_idx)
			if not r['valid']:
				print(r['message'])
				break
			v = r['value']
			if v == target:
				seq.report('exist')
				break
			cur_idx = r['next']
		else:
			seq.report('not_exist')
                '''

	if api_root!=None:
		print(get_overall_status(api_root, token))
		print('pass_token: {}'.format(get_pass_token(api_root, token)))
	else:
		for seq in seqs:
			print(seq.get_status())

# vim: foldmethod=marker
